from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def analysis_status() -> dict[str, str]:
    return {"status": "idle"}
