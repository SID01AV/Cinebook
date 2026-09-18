from fastapi import FastAPI,HTTPException,status
from starlette.status import HTTP_200_OK
from app.config import get_settings


settings = get_settings()

app= FastAPI(title=settings.app_name, debug=settings.debug)

@app.get("/health/live",status_code=status.HTTP_200_OK,tags=["health"])
async def live_check()->dict[str,str]:
    return {"status": "alive"}