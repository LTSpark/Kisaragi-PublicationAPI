from datetime import datetime
from mongoengine import Document, StringField, DateField, EmbeddedDocumentListField

from .commentary import Commentary

class Publication(Document):
    '''
    Class to define Publication Model
    '''
    author_id = StringField(required=True)
    title = StringField(required=True, max_length=100)
    content = StringField(required=True, max_length=256)
    img_url = StringField(required=False, default="")
    img_public_id = StringField(required=False, default="")
    commentaries = EmbeddedDocumentListField(Commentary)
    created_at = DateField(default=datetime.now())
