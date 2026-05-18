from fastapi import APIRouter

router = APIRouter()


@router.get("/mode")
def dj_mode() -> dict[str, str]:
    return {"mode": "prepare"}
