
from collections.abc import Sequence
from typing import TypeAlias, TypedDict
from enum import Enum, unique

GameField: TypeAlias = Sequence[Sequence[str]]

@unique
class CellOwner(Enum):
    bot = "bot"
    player = "player"

class FieldCell(TypedDict):
    owner: CellOwner
    value: str
    

