from fastapi import APIRouter

from app.schemas.mail_schema import MailSchema

# Mail Entry Point
mail_router = APIRouter()


# Mail Config
@mail_router.post("/send_mail")
async def send_sample_mail(email: MailSchema):
    # config = ConnectionConfig(
    #     MAIL_USERNAME="username",
    #     MAIL_PASSWORD="**********",
    #     MAIL_FROM="test@email.com",
    #     MAIL_PORT=587,
    #     MAIL_SERVER="mail server",
    #     MAIL_FROM_NAME="Desired Name",
    #     MAIL_STARTTLS=True,
    #     MAIL_SSL_TLS=False,
    #     USE_CREDENTIALS=True,
    #     VALIDATE_CERTS=True
    # )
    # CheckSystemLogs.pass_logs(f"isConfigCorrect: {config}", 1)
    # print(f"isConfigCorrect: {config}")
    #
    # fm = FastMail(config)
    #
    # html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """
    #
    # message = MessageSchema(
    #     subject="Fastapi-Mail module",
    #     recipients=email.email,
    #     body=html,
    #     subtype=MessageType.html)
    #
    # await fm.send_message(message)

    return {"status_code": 200, "message": f"{email.email}"}


@mail_router.post("/email_verify")
async def email_verify_email(email: MailSchema):
    return {"email": f"{email.email}"}


@mail_router.post("/resend_email_verify")
async def resend_verify_email(email: MailSchema):
    return {"email": f"{email.email}"}


@mail_router.post("/password_reset")
async def password_reset_mail(email: MailSchema):
    return {"email": f"{email.email}"}


@mail_router.post("/send_otp_code")
async def send_otp_code(otpCode: int):
    return {"otpCode": f"{otpCode}"}
