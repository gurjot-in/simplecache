from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI
from models import SimpleCache

cache = SimpleCache()
app = FastAPI()


class Item(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None
    ttl: Optional[int] = None


@app.get("/cache/{key}")
async def get_item(key: str):
    res = cache.get(key)
    return res


@app.get("/cache")
async def get_all_items():
    res = cache.get_all_keys()
    return res


@app.post("/cache")
async def create_item(item: Item):
    cache.set(key=item.key, value=item.value, ttl=item.ttl)
    return item.value


@app.delete("/cache/{key}")
async def delete_item(key: str):
    res = cache.pop(key=key)
    return res

