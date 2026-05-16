# GERARD-SEG-N-MERRCADER

Prototipo inicial de interfaz DJ estilo all-in-one con:
- 2 decks motorizados principales.
- Mixer central de 4 canales.
- Canales 3/4 conmutables entre DVS (vinilo) o CDJs externos.
- EQ por canal, FX por canal, controles de micro, auriculares y master.
- Sección de multiefectos y controles de performance (beat jump, hot cues, loops).

## 1) Probar versión web (primero)
```bash
npm run start:web
```
Luego abre: `http://localhost:8080`

## 2) Probar versión app de escritorio (después)
```bash
npm install
npm run start:app
```

## 3) Generar carpeta descargable de la app
```bash
npm run pack
```
Genera una carpeta tipo `GerardDJ-linux-x64/` lista para distribuir/probar.
