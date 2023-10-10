from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION)


@app.get('/')
def read_root():
    return {'Hello': 'FastAPI'}
