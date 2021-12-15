from typing import Optional
from fastapi import APIRouter, Depends, File, UploadFile, Form

from app.middlewares.auth import get_token_payload
from app.schemas.token_schema import TokenData
from app.services.commentary_service import CommentaryService

commentaries_router = APIRouter()

@commentaries_router.post("/commentaries", tags=["Commentaries"] )
async def create_commentary(
    payload: TokenData = Depends(get_token_payload), 
    commentary: str = Form(...),
    publication_id: str = Form(...)
):
    return await CommentaryService.create_commentary(publication_id, payload, commentary)

@commentaries_router.delete("/commentaries/{id}", tags=["Commentaries"] )
async def delete_commentary(id: str,payload: TokenData = Depends(get_token_payload), publication_id: str = Form(...)):
    return await CommentaryService.delete_commentary(publication_id, payload.id, id)
