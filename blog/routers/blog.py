from typing import List
from fastapi import APIRouter, FastAPI , Depends , status , HTTPException , Response
from sqlalchemy.orm import Session
from .. import oauth2, schemas , database , models

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)
get_db = database.get_db

from ..repository import blog

@router.get('/' , response_model=List[schemas.showblog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user) ):
    return blog.get_all(db)
    # blogs = db.query(models.Blog).all()                                    
    # return blogs


#creating a blog
@router.post('/' , status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request , db)
    # new_blog = models.Blog(title=request.title , body=request.body , user_id=1)   
    # db.add(new_blog)                                                               
    # db.commit()                                                                    
    # db.refresh(new_blog)
    # return new_blog


@router.get('/{id}' , status_code=status.HTTP_200_OK , response_model=schemas.idshowblog )
def show(id , db : Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):   
    return blog.show(id , db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()  
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} not found")
    # return blog



@router.put('/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update(id , request: schemas.Blog, db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id , request , db)
    
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"the blog body of this id {id} is not avaliable")
    # blog.update(request.dict())  #returs the dictionary of the request 
    # db.commit()
    # return 'updated'



@router.delete('/{id}' , status_code = status.HTTP_204_NO_CONTENT)
def destroy(id , db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id , db)
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"the blog not found at this id  {id}")
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return {"detail":f"Blog with the id {id} deleted successfully"}
