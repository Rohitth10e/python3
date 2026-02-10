from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantity:Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    img_url: Optional[str] = None

# List[str] :- list containing only strings
# Dict[str, int] :- string key , int value