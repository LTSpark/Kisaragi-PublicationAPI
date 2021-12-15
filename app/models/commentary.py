from mongoengine import EmbeddedDocument, StringField
from datetime import datetime
from mongoengine.fields import DateField

class Commentary(EmbeddedDocument):
    '''
    Class to define Commentary Embedded Model
    '''
    author_id = StringField(required=True)
    commentary = StringField(required=True, max_length=100)
    creation_date = DateField(default=datetime.now())
    