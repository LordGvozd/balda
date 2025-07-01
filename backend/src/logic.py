from models import CellOwner, GameField, FieldCell


def get_simple_step(field: GameField, owner: CellOwner = CellOwner.bot) -> GameField:
    """Возвращает любой валидный ход игрока или бота"""
    return field # Заглушка :)


def get_start_field(size: int) -> GameField:
    """Создает начальное поле"""
    return [
        [FieldCell(owner=CellOwner.nobody, letter=None) for col in range(size)]
        for row in range(size)
    ]
