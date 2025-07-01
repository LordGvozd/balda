from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import config
from logic import get_simple_step, get_start_field
from models import GameField


app = FastAPI(title="Balda")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)

api_router = APIRouter(prefix="/api", tags=["Api"])


@api_router.post("/bot-step")
def bot_step(current_field: GameField) -> GameField:
    """Возвращает игровое поле после хода бота"""
    return get_simple_step(current_field)


@api_router.post("/start-field")
def start_field(size: int = 5) -> GameField:
    """Возвращает стартовое игровое поле"""
    return get_start_field(size)

app.include_router(api_router)

def run_server() -> None:
    uvicorn.run(app, host=config.host, port=config.port)


if __name__ == "__main__":
    run_server()
