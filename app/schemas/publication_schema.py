from typing import Optional

from pydantic import BaseModel

class Publication(BaseModel):
    title: str
    content: str
    