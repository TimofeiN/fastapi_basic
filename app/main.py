from dataclasses import dataclass
from typing import Optional, Union

from fastapi import FastAPI

app = FastAPI()


@dataclass
class Item:
    name: str
    price: float
    description: Optional[str] = None


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Root": "Success Response!"}


@app.get("/items/{item_id}")
def read_item(
    item_id: int, q: Union[str, None] = None
) -> dict[str, Union[str, int, None]]:
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item
