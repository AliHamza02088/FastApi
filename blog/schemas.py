from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str


class showuser(BaseModel):
        name: str
        email: str
        blogs : list[Blog] = []
        class Config():
            orm_mode = True


class showblog(Blog):
        title: str
        body: str
        creator: showuser
        
        class Config():
            orm_mode = True

class idshowblog(Blog):
    title: str
    body: str


class login(BaseModel):
    username: str
    password: str 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
