from app.database.config import connect_database
from app.models.publication import Publication

connect_database()

async def create_publication(author_id, title, content, url, public_id):

    new_publication = Publication(
        title=title, 
        content=content,
        author_id=author_id,
        img_url=url,
        img_public_id=public_id
    )
    
    new_publication.save()


    