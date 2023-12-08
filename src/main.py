from fastapi import FastAPI

from src.posts.routes import router as posts_router

from src.posts.models import Posts

app = FastAPI()

app.include_router(posts_router)


@app.on_event("startup")
def startup():
    Posts.create_table()
