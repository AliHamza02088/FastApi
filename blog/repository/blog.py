from sqlalchemy.orm import Session
from .. import models , schemas
from fastapi import status , HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()                                    
    return blogs

def create(request: schemas.Blog , db):
    new_blog = models.Blog(title=request.title , body=request.body , user_id=1)   
    db.add(new_blog)                                                               
    db.commit()                                                                    
    db.refresh(new_blog)
    return new_blog


def destroy(id , db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"the blog not found at this id  {id}")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail":f"Blog with the id {id} deleted successfully"}


def update(id ,request: schemas.Blog ,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"the blog body of this id {id} is not avaliable")
    blog.update(request.dict())  #returs the dictionary of the request 
    db.commit()
    return 'updated'

def show(id , db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()  
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} not found")
    return blog