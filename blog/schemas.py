from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
class ShowBlog(BaseModel):
    title: str
    body : str
    additional_information : str = "You can read more information here"
    class Config:
        orm_mode=True
