from fastapi import APIRouter

router = APIRouter()

@router.get("/health/liveness")
async def liveness():
    return {"status": "alive"}

@router.get("/health/readiness")
async def readiness():
    return {"status": "ready"}
