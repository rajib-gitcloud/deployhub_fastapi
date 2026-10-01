from typing import List, Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()

class Item(BaseModel):
    id: int
    title: str = Field(..., example="Setup FastAPI")
    description: Optional[str] = None
    completed: bool = False

# In-memory item store
ITEMS_DB: List[Item] = [
    Item(id=1, title="Initialize FastAPI Starter", description="Set up modern asynchronous API structure", completed=True),
    Item(id=2, title="Configure DeployHub Manifest", description="Define port 8000 and healthcheck endpoint", completed=True),
    Item(id=3, title="Deploy to Cloud", description="Ship containerized microservice", completed=False)
]

@router.get("/items", response_model=List[Item])
async def list_items():
    return ITEMS_DB

@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in ITEMS_DB:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {item_id} not found")

@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    for existing in ITEMS_DB:
        if existing.id == item.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Item with ID {item.id} already exists")
    ITEMS_DB.append(item)
    return item
