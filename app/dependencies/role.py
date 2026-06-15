from fastapi import HTTPException, status
from fastapi import Depends

from app.dependencies.auth import get_current_user

def require_roles(*roles):
    def dependency(current_user = Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return current_user
    return dependency