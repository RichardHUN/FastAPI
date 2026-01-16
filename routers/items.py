from fastapi import APIRouter, HTTPException, status
from models.item import Item, Item_Response
from typing import List


router = APIRouter()

# Mock database of items
items = [
    {"id": 1, "name": "Item 1", "description": "First item", "price": 10.99},
    {"id": 2, "name": "Item 2", "description": "Second item", "price": 20.50},
    {"id": 3, "name": "Item 3", "description": None, "price": 15.75},
]


@router.get("/", response_model=List[Item_Response])
def get_items():
    """Return a list of all available items."""
    return items


@router.get("/{item_id}", response_model=Item_Response)
def get_item(item_id: int):
    """Return an item by its ID."""
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id {item_id} not found"
    )


@router.post("/", response_model=Item_Response, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    """Create a new item. Return 400 if the id already exists."""
    for existing_item in items:
        if existing_item["id"] == item.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Item with id {item.id} already exists"
            )
    
    new_item = item.dict()
    items.append(new_item)
    return new_item


@router.put("/{item_id}", response_model=Item_Response, status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):
    """Update an item by ID or raise 404."""
    for i, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            updated_item = item.dict()
            items[i] = updated_item
            return updated_item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id {item_id} not found"
    )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """Remove item by ID or raise 404."""
    for i, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(i)
            return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id {item_id} not found"
    )
