from fastapi import HTTPException

from app.database.config import connect_database
from app.models.publication import Publication
from app.models.commentary import Commentary

connect_database()

class CommentaryService:
    '''
    Class with methods to manage commentaries operation
    '''
    @staticmethod
    async def create_commentary(publication_id, author, commentary):
        publication_obj = Publication.objects(
            id=publication_id,
        ).first()

        if publication_obj is None:
            raise HTTPException(status_code=400, detail="Publication not found")
        new_commentary = Commentary(
            author_id=author.id,
            commentary=commentary
        )
        publication_obj.commentaries.append(new_commentary)
        publication_obj.save()
        return { "msg": "Commentary created successfully" }
    
    @staticmethod
    async def delete_commentary(publication_id, author_id, commentary_id):
        publication_obj = Publication.objects(id=publication_id).first()

        if publication_obj is None:
            raise HTTPException(status_code=400, detail="Publication not found")

        commentary_list = publication_obj.commentaries.filter(_id=commentary_id, author_id=author_id)

        if not commentary_list:
            raise HTTPException(status_code=400, detail="Commentary not found")
        
        commentary = commentary_list[0]
        publication_obj.commentaries.remove(commentary)
        #publication_obj.save()

        return { "msg": "Commentary deleted successfully" }

        
        
        