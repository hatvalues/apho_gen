"""End point for the main apho application"""
from fastapi import APIRouter
from app_logic.inflect_words import get_plurals
from pydantic import BaseModel

class SimpleDictionaryResponse(BaseModel):
    data: dict

# API route
router = APIRouter()

@router.get('/v1/pluralize/{text}', status_code=200)
async def pluralize(text: str):
    """Gets a dict of plural words from text.
    Some are not valid"""
    return SimpleDictionaryResponse(data=get_plurals(text))
