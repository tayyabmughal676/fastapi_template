import sys
import uvicorn

"""
    @args:
        --prod: production mode
"""

if __name__ == '__main__':
    is_prod = '--prod' in sys.argv

    uvicorn.run(
        app='app.app:app',
        host='0.0.0.0',
        port=8000,
    )
