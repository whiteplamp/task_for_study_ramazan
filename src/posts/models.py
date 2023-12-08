import uuid

from src.db.common import BaseModel
from peewee import UUIDField, TextField, IntegerField


class Posts(BaseModel):
    id = UUIDField(null=False, unique=True, primary_key=True, default=uuid.uuid4)
    text = TextField(null=False)
    likes = IntegerField(null=False, default=0)
    dislikes = IntegerField(null=False, default=0)

    class Meta:
        table_name = "posts"

