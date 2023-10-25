from typing import Dict

from fastapi import APIRouter
from loguru import logger

agents_router = APIRouter(prefix="/agents")


@agents_router.post("/user/")
async def user(message: str) -> Dict[str, str]:
    reversed_message = message[::-1]
    logger.debug(f"User Message Reversed: {reversed_message}")
    return {"String Successfully Reversed": f"{reversed_message}"}
