from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session

router = APIRouter()


@router.get("/")
def read_entities(
    db: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve entities.
    """
    entities = []
    # get entities from db
    return entities


@router.get("/{id}")
def read_entity(
    *,
    db: AsyncSession = Depends(get_session),
    id: int,
) -> Any:
    """
    Get by ID.
    """
    entity = {}
    # get entity from db
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return entity


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_entity(
    db: AsyncSession = Depends(get_session),
) -> Any:
    """
    Create new entity.
    """
    entity = {}
    # create item by params
    return entity


@router.put("/{id}")
def update_entity(
    *,
    db: AsyncSession = Depends(get_session),
    id: int
) -> Any:
    """
    Update an entity.
    """
    entity = {}
    # get entity from db
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # update entity in db
    return entity


@router.delete("/{id}")
def delete_entity(
    *,
    db: AsyncSession = Depends(get_session),
    id: int
) -> Any:
    """
    Delete an entity.
    """
    entity = {}
    # get entity from db
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # remove item from db
    return entity