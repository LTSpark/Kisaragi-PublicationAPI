from os import stat
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
    async def create_commentary(publication_id, author_id, commentary):
        publication_obj = Publication.objects(
            id=publication_id,
        ).first()

        if publication_obj is None:
            raise HTTPException(status_code=400, detail="Publication not found")
        new_commentary = Commentary(
            author_id=author_id,
            commentary=commentary
        )
        publication_obj.commentaries.append(new_commentary)
        publication_obj.save()
        return { "msg": "Commentary created successfully" }
    
    @staticmethod
    async def delete_commentary(publication_id, author_id, commentary_id):
        publication_obj = Publication.objects(
            id=publication_id,
            author_id=author_id
        ).first()
        commentary = list(filter(lambda commentary: commentary.to_dict()['_id'] == commentary_id, publication_obj.commentaries))[0]
        if commentary in publication_obj.commentaries:
            publication_obj.commentaries.remove(commentary)
            publication_obj.save()
            return { "msg": "Commentary deleted successfully" }
        raise HTTPException(status_code=400, detail="Commentary not found")
        
        