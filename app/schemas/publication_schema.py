from datetime import date
from typing import List, Optional

from pydantic import BaseModel

class Commentary(BaseModel):
    _id: str
    commentary: str
    author_id: str
    created_at: date

class Publication(BaseModel):
    _id: str
    title: str
    content: str
    author_id: str
    img_url: str
    commentaries: Optional[List[Commentary]] = None
    created_at: date
