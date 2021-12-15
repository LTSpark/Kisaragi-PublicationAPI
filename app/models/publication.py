from datetime import datetime
from mongoengine import Document, StringField, DateField, EmbeddedDocumentListField

from .commentary import Commentary

class Publication(Document):
    '''
    Class to define Publication Model
    '''
    author_id = StringField(required=True)
    author_name = StringField(required=True)
    title = StringField(required=True, max_length=100)
    content = StringField(required=True, max_length=256)
    img_url = StringField(required=False, default="")
    img_public_id = StringField(required=False, default="")
    commentaries = EmbeddedDocumentListField(Commentary)
    created_at = DateField(default=datetime.utcnow)

    def to_json(self):
        publication_dict = {
            "publication_id": str(self.pk),
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "author_name": self.author_name,
            "img_url": self.img_url,
            "created_at": self.created_at,
            "commentaries": list(map(lambda commentary: commentary.to_dict(), self.commentaries))
        }
        return publication_dict
