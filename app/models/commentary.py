from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import EmbeddedDocument, StringField, DateField, ObjectIdField

class Commentary(EmbeddedDocument):
    '''
    Class to define Commentary Embedded Model
    '''
    _id = ObjectIdField( required=True, default=ObjectId )
    author_id = StringField(required=True)
    commentary = StringField(required=True, max_length=100)
    created_at = DateField(default=datetime.utcnow)
    def to_dict(self):
        commentary_dict = {
            "commentary_id": str(self._id),
            "author_id": self.author_id,
            "commentary": self.commentary,
            "created_at": self.created_at
        }
        return commentary_dict