import os

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from jose import JWTError, jwt
from dotenv import load_dotenv

from app.schemas.token_schema import TokenData

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

security = HTTPBearer()

async def get_token_payload(credentials: HTTPBasicCredentials = Depends(security)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = credentials.credentials
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("id")
        user_name: str = payload.get("name")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id=user_id, name=user_name)
    except JWTError:
        raise credentials_exception
    
    return token_data
    