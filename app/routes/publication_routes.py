import os
import cloudinary
import cloudinary.uploader

from typing import Optional
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, File, UploadFile, Form

from app.middlewares.auth import get_token_payload
from app.schemas.token_schema import TokenData
from app.services.publication_service import create_publication

load_dotenv()

cloudinary.config(
    cloud_name = os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    secure=True
)

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
    upload_result = cloudinary.uploader.upload(file_readed)
    url = upload_result["url"]
    public_id = upload_result["public_id"]
    await create_publication(payload.id, title, content, url, public_id)
    return { "msg": "hola"}

