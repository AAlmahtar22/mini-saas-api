from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.deps import get_db
from app.models.models import User
from app.schemas.schemas import UserCreate, UserLogin
from app.services.auth import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
     existing_user = db.query(User).filter(User.email == user.email).first()
     if existing_user:
         raise HTTPException(
             status_code=status.HTTP_400_BAD_REQUEST, 
             detail="Email already registered"
         )
     hashed_pw = hash_password(user.password)
     
     new_user = User( 
         email=user.email,
         password=hashed_pw
     )
     try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

     except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Email already exists"
            )
     return {"message": "User created", "email": new_user.email}


@router.post("/login")
def login(
    user: UserLogin, # <-- This forces Swagger to show a JSON text block
    db: Session = Depends(get_db)
):
    # Query your database using the email property from your Pydantic JSON schema
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid credentials"
        )

    # Verify using the plain password string sent in your JSON request payload
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid credentials"
        )

    token = create_access_token({"user_id": db_user.id})
    
    return {"access_token": token, "token_type": "bearer"}
