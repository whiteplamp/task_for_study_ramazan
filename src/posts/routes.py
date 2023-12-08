from fastapi import APIRouter

from src.posts.schemas import Post

from src.posts.models import Posts

router = APIRouter()


@router.get("/posts")
def get_posts():
    return [1, 2, 3, 4, 5]


@router.post("/posts")
def create_post(post: Post):
    post_id = Posts.insert({
        "text": post.text
    }).execute()
    return post_id
