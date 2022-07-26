from fastapi import APIRouter
from .. import util

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/{name}")
async def read_item(name):
    return {"item_id": name}