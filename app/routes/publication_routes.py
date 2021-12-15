from typing import Optional
from fastapi import APIRouter, Depends, File, UploadFile, Form

from app.middlewares.auth import get_token_payload
from app.schemas.token_schema import TokenData
from app.services.publication_service import PublicationService

publications_router = APIRouter()

@publications_router.post(
    "/publications",
    tags=["Publications"]
)
async def post_publication(
    title: str = Form(...),
    content: str = Form(...),
    payload: TokenData = Depends(get_token_payload), 
    file: Optional[UploadFile] = File(...)
):
    file_readed = await file.read()
    await PublicationService.create_publication(payload.id, title, content, file_readed)
    return { "msg": "Publication created successfully" }

