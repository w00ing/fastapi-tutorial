from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND


from blog.hashing import Hash
from .. import database, models, token

router = APIRouter(
    tags=["auth"],
)


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    access_token = token.create_access_token(data={"sub": user.email, "id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
