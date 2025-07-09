from fastapi import APIRouter, FastAPI

router = APIRouter()


def setup_routers(app: FastAPI) -> None:
    app.include_router(router)
