from fastapi import FastAPI

from src.posts.routes import router as posts_router

app = FastAPI()

app.include_router(posts_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
