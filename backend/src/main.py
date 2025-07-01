from fastapi import FastAPI, APIRouter
import uvicorn

from logic import get_simple_step
from models import GameField


app = FastAPI(title="Balda")
api_router = APIRouter(prefix="/api", tags=["Api"])


@api_router.get("/bot-step")
def bot_step(current_field: GameField) -> GameField:
    """Возвращает игровое поле после хода бота"""
    return get_simple_step(current_field)

def run_server() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run_server()



