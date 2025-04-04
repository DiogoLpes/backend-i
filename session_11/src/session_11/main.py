from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.post("/items/")
async def create_item(item: str):
    logger.info(f"Item received: {item}")
    # A simple validation example
    if "name" not in item:
        logger.error("Item does not contain 'name'")
        raise HTTPException(status_code=400, detail="Item must have a name")
    return {"item": item}

@app.put("/items/{item_id}")
async def update_id(item_id: int, item: Item):
    logger.info("Update endpoint called")
    return {"Item_name": item.name, "item_id": item_id}
# Run the application using Uvicorn with:
# poetry run uvicorn main:app --reload