from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from blog import schemas, database
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=["users"],
)


@router.post("/")
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)
