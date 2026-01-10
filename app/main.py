from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting lifespan")

    yield   # 서버가 작동하는 구간

    print("Stopping lifespan")

app = FastAPI(
    title="Note Service",
    description="Note Service",
    version="1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(None, prefix="/notes", tags=["Note"])



if __name__ == '__main__':
    print("Starting app")
    uvicorn.run("app.main:app", host="127.0.0.1", port=9900, reload=True)