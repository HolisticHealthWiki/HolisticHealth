from fastapi import APIRouter

from HolisticHealth.api.v1 import v1_router

api_router = APIRouter(prefix="/api")

api_router.include_router(router=v1_router, tags=["v1"])
