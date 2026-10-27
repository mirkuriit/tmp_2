from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.config import Settings, settings
from src.middleware import LogMiddleware
from src.routers.v1.moderation_decision_router import (
    router as moderation_decision_router_v1,
)


def make_lifespan(settings: Settings):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        engine = create_async_engine(settings.postgres_url, pool_pre_ping=True)
        app.state.db_engine = engine
        app.state.SessionFactory = async_sessionmaker(engine, expire_on_commit=False)

        try:
            yield
        finally:
            await engine.dispose()

    return lifespan

def add_routers(app: FastAPI) -> None:
    app.include_router(moderation_decision_router_v1)


def add_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    app.add_middleware(LogMiddleware)

def get_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        docs_url='/docs',
        openapi_url='/openapi.json',
        default_response_class=JSONResponse,
        lifespan=make_lifespan(settings),
    )
    app.state.settings = settings

    add_routers(app)
    add_middlewares(app)

    return app

app = get_app(settings)