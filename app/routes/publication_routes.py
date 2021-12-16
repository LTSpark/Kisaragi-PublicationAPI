from typing import Optional
from fastapi import APIRouter, Depends, File, UploadFile, Form

from app.middlewares.auth import get_token_payload
from app.schemas.token_schema import TokenData
from app.schemas.publication_schema import Publication
from app.services.publication_service import PublicationService

publications_router = APIRouter()

@publications_router.post("/publications", tags=["Publications"])
async def post_publication(
    title: str = Form(...),
    content: str = Form(...),
    payload: TokenData = Depends(get_token_payload), 
    file: Optional[UploadFile] = File(...)
):
    file_readed = await file.read()
    await PublicationService.create_publication(payload, title, content, file_readed)
    return { "msg": "Publication created successfully" }

@publications_router.delete("/publications/{id}", tags=["Publications"])
async def delete_publication(id: str, payload: TokenData = Depends(get_token_payload)):
    message = await PublicationService.delete_publication(id, payload.id)
    return { "msg": message }

@publications_router.get("/publications/{id}/id", tags=["Publications"], response_model=Publication)
async def get_publication(id: str):
    return await PublicationService.get_publication(id)

@publications_router.get("/publications", tags=["Publications"], response_model=list[Publication])
async def get_publications(skip: int = 0, limit: int = 5):
    return await PublicationService.get_publications(skip, limit)

@publications_router.get("/publications/hashtags", tags=["Publications"], response_model=list[Publication])
async def get_publications_by_hashtag(skip: int = 0, limit: int = 5, hashtag: str = None):
    return await PublicationService.get_publications_by_hashtag(skip, limit, hashtag)
