from fastapi.routing import APIRouter
from fastapi import Response
from .schemas import Schema
from .db import aggregate, get_data

router = APIRouter()


@router.post("/items/")
def aggregate_data(item: Schema):
    res = aggregate(item=item)
    # for i in res:
    #     print(i.id)
    return {1:1}


@router.get("/items/")
def get_all():
    res = get_data()
    print(res)
    return {1:1}

