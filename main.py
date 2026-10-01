from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI ()

class Item(BaseModel):
    name    : Optional[str] = None
    alamat  : Optional[str] = None
    IPK     : Optional[float] = None
    semester: Optional[int] = None
    hobi    : Optional[str] = None

item_db= {}

@app.get("/")
def read_root():
    return { "massage:", "helo world!"}

@app.post("/Item/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in item_db:
        return {"eror": "items is already exits"}
    item_db[item_id] = item.dict()
    return {'message': "item created succesfully", "item": item_db [item_id]}

@app.get("/Item/{item_id}")
async def read_item(item_id: int):
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail= "wle 👅\n items is not found")
    return {'item_id': item_id, "item": item_db [item_id]}

@app.put("/Item/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in item_db:
        return {"eror": "wle 👅\n items not found"}
    item_db[item_id] = item.dict()
    return {'message': "item created succesfully", "item": item_db [item_id]}

@app.delete("/Item/{item_id}")
async def delete_item(item_id: int):
    if item_id not in item_db:
        return {"eror": "wle 👅\n items not found"}
    delete_item = item_db.pop(item_id)
    return {'message': "item delete succesfully ✨✨✨", "deeleted_item": delete_item}

