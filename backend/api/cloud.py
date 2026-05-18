from fastapi import APIRouter

router = APIRouter()


@router.get("/providers")
def providers() -> list[str]:
    return ["google_drive", "dropbox", "onedrive"]
