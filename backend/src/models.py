from collections.abc import Sequence
from typing import TypeAlias, TypedDict
from enum import Enum, unique


@unique
class CellOwner(Enum):
    bot = "bot"
    player = "player"
    nobody = "nobody"


class FieldCell(TypedDict):
    owner: CellOwner
    letter: str | None


GameField: TypeAlias = Sequence[Sequence[FieldCell]]
