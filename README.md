# MUSIC_BOX

Arquitectura base para una app de gestión musical con backend FastAPI, núcleo modular en Python y apps cliente (desktop/web).

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## Estructura

- `backend/`: API FastAPI y servicios de aplicación.
- `music_box/`: dominio principal (DB, audio, análisis, integraciones).
- `workers/`: workers asíncronos/scheduled.
- `scripts/`: utilidades operativas.
- `docs/`: documentación viva.
