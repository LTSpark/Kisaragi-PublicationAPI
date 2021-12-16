import os
import cloudinary
import cloudinary.uploader

from dotenv import load_dotenv
from fastapi import HTTPException

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
    '''
    Class with methods to manage publication operations
    '''
    @staticmethod
    async def create_publication(author, title, content, file):
        upload_result = cloudinary.uploader.upload(file, folder="kisaragi_publications")
        url = upload_result["url"]
        public_id = upload_result["public_id"]
        new_publication = Publication(
            title=title, 
            content=content,
            author_id=author.id,
            img_url=url,
            img_public_id=public_id
        )       
        new_publication.save()
    
    @staticmethod
    async def delete_publication(publication_id, author_id):
        publication_obj = Publication.objects(
            id=publication_id,
            author_id=author_id
        ).first()

        if publication_obj is not None:
            cloudinary.uploader.destroy(publication_obj.img_public_id)
            publication_obj.delete()
            return "Publication deleted successfully"
        raise HTTPException(status_code=400, detail="Publication not found")
    
    @staticmethod
    async def get_publication(publication_id):
        publication_obj = Publication.objects(
            id=publication_id,
        ).first()

        if publication_obj is not None:
            return publication_obj.to_json()
        raise HTTPException(status_code=400, detail="Publication not found")
    
    @staticmethod
    async def get_publications(skip, limit):
        publication_objs = Publication.objects().limit(limit).skip(skip)
        publications = []
        publications = list(map(lambda publication_obj: publication_obj.to_json(), publication_objs))
        return publications

