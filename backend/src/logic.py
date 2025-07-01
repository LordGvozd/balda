
from models import CellOwner, GameField


def get_simple_step(field: GameField, owner: CellOwner = CellOwner.bot) -> GameField:
    """Возвращает любой валидный ход игрока или бота"""
    return field
