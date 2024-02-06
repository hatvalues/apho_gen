"""End point for the main apho application"""
from fastapi import APIRouter
from app_logic.apho_gen import get_apho_for_name
from pydantic import BaseModel

class SimpleResponse(BaseModel):
    message: str


# API route
router = APIRouter()

@router.get('/v1/feel-good/{name}', status_code=200)
async def get_apho(name):
    return SimpleResponse(message=get_apho_for_name(name))
