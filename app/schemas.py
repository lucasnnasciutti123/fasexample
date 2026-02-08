from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic import conint, Field


class Post(BaseModel):
    title: str
    content: str
    published: bool = True



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    votes: int = 0  # ← Adicione este campo
    
    class Config:
        from_attributes = True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    votes: int

    class Config:
        from_attributes = True

class PostOut(PostBase):
    Post: PostResponse
    votes: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str




class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: int = Field(le=1, ge=0)