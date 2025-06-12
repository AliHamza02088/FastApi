from fastapi import FastAPI , APIRouter
from blog import  models 
from blog.database import engine
from .routers import blog , user , authentication

app = FastAPI()
router = APIRouter()


models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)
















# from typing import List
# from fastapi import FastAPI , Depends , status , Response , HTTPException 
# from blog import schemas , models , hashing
# from sqlalchemy.orm import Session
# from blog.database import sessionlocal , get_db
# from .hashing import Hash


#this is use for database new connection when user hit a request and this work every time when user hit a request and after than close
# def get_db():
#     db = sessionlocal()
#     try:
#         yield db
#     finally:
#         db.close()


#database connection injected that why we import depends from fastapi
#creating a blog
# @app.post('/blog' , status_code=status.HTTP_201_CREATED , tags=['blogs'])
# def create(request: Blog, db : Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title , body=request.body , user_id=1)  #json requets from user/client
#     db.add(new_blog)                                                             #add into new blog section
#     db.commit()                                                                  #database inject
#     db.refresh(new_blog)
#     return new_blog


#get all data from database
# @app.get('/blog' , response_model=list[schemas.showblog] , tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()                                    #query means get all data from blog table
#     return blogs



# @app.get('/blog/{id}' , status_code=status.HTTP_200_OK , response_model=schemas.idshowblog , tags=['blogs'])
# def show(id , response: Response , db : Session = Depends(get_db)):    #get the id from user , response is used to set the status code
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()  #get the first blog with the id
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail":f"blog with the id {id} not found"}
#     return blog



# @app.put('/blog/{id}' , status_code=status.HTTP_202_ACCEPTED , tags=['blogs'])
# def update (id , request: Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"the blog body of this id {id} is not avaliable")
#     blog.update(request.dict())  #retunrs the dictionary of the request 
#     db.commit()
#     return 'updated'



# @app.delete('/blog/{id}' , status_code = status.HTTP_204_NO_CONTENT , tags=['blogs'])
# def destroy(id , db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"the blog not found at this id  {id}")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {"detail":f"Blog with the id {id} deleted successfully"}










# @app.post('/user' , response_model=schemas.showuser , tags=['users'])
# def create_user(request: schemas.User , db : Session = Depends(get_db)):
#     new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/user' , response_model=schemas.showuser , tags=['users'])
# def get(id:int , db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} not found")
#     return user

