from peewee import PostgresqlDatabase, Model

from src.db.config import (
    DB_USER,
    DB_PORT,
    DB_NAME,
    DB_PASS,
    DB_HOST,
)

if not all((DB_USER, DB_PORT, DB_NAME, DB_PASS, DB_HOST)):
    exit("Set up db_properties in environment file")

database = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)


class BaseModel(Model):
    class Meta:
        database = database







