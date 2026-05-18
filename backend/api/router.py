from fastapi import APIRouter

from backend.api import analysis, cloud, dj, playlists, social, tracks

api_router = APIRouter()
api_router.include_router(tracks.router, prefix="/tracks", tags=["tracks"])
api_router.include_router(playlists.router, prefix="/playlists", tags=["playlists"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
api_router.include_router(cloud.router, prefix="/cloud", tags=["cloud"])
api_router.include_router(dj.router, prefix="/dj", tags=["dj"])
api_router.include_router(social.router, prefix="/social", tags=["social"])
