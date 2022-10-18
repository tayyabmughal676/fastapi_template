from fastapi import APIRouter, Depends, HTTPException, status, Body
from app.schemas.token_schema import TokenSchema
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token, create_refresh_token
from app.schemas.user_schema import UserOut
from jose import jwt
from app.api.deps.user_deps import get_current_user
from app.core.security import settings
from app.models.user_models.user_model import UserModel
from app.schemas.token_schema import TokenPayload
from app.services.user_services.user_service import UserService
from pydantic import ValidationError
from typing import Any

# Auth Route Entry point.
auth_router = APIRouter()


# response_model=TokenSchema
@auth_router.post("/login", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    print(f"formData: {form_data.username}, {form_data.password}")
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    accessToken = create_access_token(user.user_id)
    refreshToken = create_refresh_token(user.user_id)

    return {
        "access_token": accessToken,
        "refresh_token": refreshToken,
    }

    # return {
    #     "code": 1,
    #     "message": "Success",
    #     "data": {
    #         "access_token": accessToken,
    #         "refresh_token": refreshToken,
    #         "user": user,
    #     }
    # }


@auth_router.get('/test-token', response_model=UserOut)
def test_token(user: UserModel = Depends(get_current_user)):
    return user


@auth_router.post('/refresh', response_model=TokenSchema)
async def refresh_token(refresh_user_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_user_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid token for user",
        )
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }
