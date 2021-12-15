import os
import cloudinary
import cloudinary.uploader

from dotenv import load_dotenv

from app.database.config import connect_database
from app.models.publication import Publication

load_dotenv()
connect_database()

cloudinary.config(
    cloud_name = os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    secure=True
)

class PublicationService:
    @staticmethod
    async def create_publication(author_id, title, content, file):
        upload_result = cloudinary.uploader.upload(file)
        url = upload_result["url"]
        public_id = upload_result["public_id"]
        new_publication = Publication(
            title=title, 
            content=content,
            author_id=author_id,
            img_url=url,
            img_public_id=public_id
        )       
        new_publication.save()


    