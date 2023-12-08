from fastapi import APIRouter


router = APIRouter()


@router.get("/posts")
def get_posts():
    return [1, 2, 3, 4, 5]
