from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_playlists() -> list[dict[str, str]]:
    return [{"id": "p1", "name": "Warmup"}]
