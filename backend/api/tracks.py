from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_tracks() -> list[dict[str, str]]:
    return [{"id": "1", "title": "Demo Track"}]
