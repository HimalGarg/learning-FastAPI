from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: str

inventory = {
    1: Item(**{'name':'milk' ,
        "price" : 50,
        "brand" : "Amul"
        })
}



@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path (description="ID of the item")):
    if item_id not in inventory:
        return {"Item":"does not exist"}
    return inventory[item_id]

@app.get("/get-by-name")
def get_by_name(name: str = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data":"Not Found"}

@app.post("/create-item/{item_id}")
def create_item(item: Item, item_id: int = Path(description="ID of the new object")):

    if item_id in inventory:
        return {"Item":"already exists"}
    

    inventory[item_id] = item

    return item


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Item":"does not exist"}
    
    inventory[item_id] = item
    return "Updated Successfully"


@app.delete("/delete-item")
def delete_item(item_id : int = Query(...,description="ID of the item to be deleted")):
    if item_id not in inventory:
        return {"Item":"does not exist"}
    
    del inventory[item_id]
    return {"itemDeleted" : "Successfully"}


    
    