from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import configure_logging, settings

app = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION)
app.include_router(main_router)


@app.on_event("startup")
async def startup():
    configure_logging()
