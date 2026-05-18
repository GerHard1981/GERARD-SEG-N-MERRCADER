from fastapi import APIRouter

router = APIRouter()


@router.get("/channels")
def channels() -> list[str]:
    return ["instagram", "tiktok", "youtube"]
