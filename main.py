from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from database import init_db
from routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


check_app = FastAPI()
check_app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(check_app, port=8000, host='127.0.0.1')