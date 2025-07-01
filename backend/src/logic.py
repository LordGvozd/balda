from dataclasses import dataclass
from pprint import pprint
from typing import Self

from models import CellOwner, GameField, FieldCell
from words import get_random

# @dataclass
# class FieldNode:
#     letter: str | None
#
#     ns: list[Self]
#
#
# def get_tree_by_field(field: GameField) -> FieldNode:
#     def get_node(coords: tuple[int, int], processed: list[tuple[int, int]], branch: str) -> FieldNode:
#
#         pre_coords = []
#             (coords[0], coords[1] - 1),
#             (coords[0], coords[1] + 1),
#             (coords[0] - 1, coords[1]),
#             (coords[0] + 1, coords[1]),
#         ]
#
#         n_coords = []
#
#
#         for coord in pre_coords:
#             if coord in processed:
#                 continue
#
#             if (0 <= coord[0] < len(field)) and (0 <= coord[1] < len(field) - 1):
#                 if field[coord[1]][coord[0]]["letter"] == None:
#                     continue
#                 else:
#                     n_coords.append(coord)
#
#         processed.extend(n_coords)
#
#         ns = [get_node(n, processed, branch + str(field[coords[1]][coords[0]]["letter"])) for n in n_coords]
#
#         node = FieldNode(
#             letter = field[coords[1]][coords[0]]["letter"],
#             ns=ns
#         )
#
#         return node
#
#     root = get_node((2, 2), [], "")
#     print(root.ns)
#
#     return root
#


def get_simple_step(field: GameField, owner: CellOwner = CellOwner.bot) -> GameField:
    """Возвращает любой валидный ход игрока или бота"""
    return field # Заглушка :)




def get_start_field(size: int) -> GameField:
    """Создает начальное поле"""
    field = [
        [FieldCell(owner=CellOwner.nobody, letter="") for col in range(size)]
        for row in range(size)
    ]
    
    for index, letter in enumerate(get_random(size)):
        field[size // 2][index]["letter"] = letter

    return field


def print_field(field: GameField) -> None:
    pprint([[f"{cell['letter'] if cell['letter'] is not None else ' '}" for cell in row] for row in field])




@dataclass
class Node:
    letter: str
    neighbours: list[Self]




def get_all_words(field: GameField) -> set[str]:
    def _get_neighbours(target: tuple[int, int], processed_targets: list) -> list[Node]:
        if target in processed_targets:
            return

        LEFT = (target[0] - 1, target[1]) if target[0] != 0 else None
        RIGHT = (target[0] + 1, target[1]) if target[0] != 5 - 1 else None
        UP = (target[0], target[1] - 1) if target[1] != 0 else None
        BOTTOM = (target[0], target[1] + 1) if target[1] != 5 - 1 else None

        neighbours_coords = [n for n in (LEFT, UP, BOTTOM, RIGHT) if n is not None and field[n[1]][n[0]]["letter"] != ""]
        return [
            Node(
                letter=field[c[1]][c[0]]["letter"],
                neighbours=_get_neighbours(c, [*processed_targets, target])
            ) for c in neighbours_coords
        ]

    words = []
    def _get_word(target: Node, word: str):
        for n in target.neighbours:
            if n.neighbours is not None:
                _get_word(n, word + n.letter)
            else:
                words.append(word)


    for y in range(len(field)):
        for x in range(len(field)):
            target = (x, y)
            root = Node(
                letter=field[target[1]][target[0]]["letter"],
                neighbours=_get_neighbours(target, [])
            )
            _get_word(root, root.letter)

    return (set(words))




field = get_start_field(5)

print_field(field)
pprint(get_all_words(field))

