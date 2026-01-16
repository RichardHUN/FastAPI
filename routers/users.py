from fastapi import APIRouter, HTTPException, status
from models.user import User, User_Response
from typing import List


router = APIRouter()

# Mock database of users
users = [
    {"id": 1, "username": "john_doe", "email": "john@example.com", "full_name": "John Doe", "is_active": True},
    {"id": 2, "username": "jane_smith", "email": "jane@example.com", "full_name": "Jane Smith", "is_active": True},
    {"id": 3, "username": "bob_wilson", "email": "bob@example.com", "full_name": None, "is_active": False},
]


@router.get("/", response_model=List[User_Response])
def get_users():
    """Return all users."""
    return users

@router.get("/{user_id}", response_model=User_Response)
def get_user(user_id: int):
    """Return a full user by ID or raise 404."""
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} not found"
    )

@router.post("/", response_model=User_Response, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    """Create a new user. Return 400 if the id already exists."""
    for existing_user in users:
        if existing_user["id"] == user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with id {user.id} already exists"
            )
    
    new_user = user.dict()
    users.append(new_user)
    return new_user


@router.put("/{user_id}", response_model=User_Response, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: User):
    """Update a user by ID or raise 404."""
    for i, existing_user in enumerate(users):
        if existing_user["id"] == user_id:
            updated_user = user.dict()
            users[i] = updated_user
            return updated_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} not found"
    )

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    """Remove user by ID or raise 404."""
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} not found"
    )
