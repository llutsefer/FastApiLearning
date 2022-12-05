from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str
class Blog(BlogBase):
    class Config:
        orm_mode=True
class User(BaseModel):
    name:str
    email:str
    password:str
class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog] = []
    class Config:
        orm_mode=True
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    additional_information : str = "You can read more information here"
    class Config:
        orm_mode=True