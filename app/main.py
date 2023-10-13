from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.api.routers import main_router
from app.core.config import configure_logging, settings

app = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION)
app.include_router(main_router)


@app.on_event("startup")
async def startup():
    configure_logging()
    add_pagination(app)
