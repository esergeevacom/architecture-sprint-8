import uvicorn
from src.base.bootstrap import build_app
from src.base.settings import settings

app = build_app()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # nosec
        port=int(settings.port),
    )
