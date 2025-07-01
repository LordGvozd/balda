from dataclasses import dataclass
from pprint import pprint
from typing import Self

from models import CellOwner, GameField, FieldCell
from words import *



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
    pprint([[f"{cell['letter'] if cell['letter'] != "" else ' '}" for cell in row] for row in field])




@dataclass
class Node:
    letter: str
    neighbours: list[Self]
    coord: tuple[int, int]


def get_neighbours(target: tuple[int, int], processed_targets: list) -> list[Node]:
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
            neighbours=get_neighbours(c, [*processed_targets, target]),
            coord=target
        ) for c in neighbours_coords
    ]



def get_all_words(field: GameField) -> list[list[Node]]:
    words = []
    def _get_word(target: Node, word: str):
        for n in target.neighbours:
            if n.neighbours is not None:
                
                _get_word(n, [*word, n])
            else:
                if word in words:
                    return
                words.append(word)


    for y in range(len(field)):
        for x in range(len(field)):
            target = (x, y)
            root = Node(
                letter=field[target[1]][target[0]]["letter"],
                neighbours=get_neighbours(target, []),
                coord=target
            )
            _get_word(root, [root, ])
    
    return words

def node_list_to_str(node_list: list[Node]) -> list[str]:
    return ["".join([n.letter for n in word]) for word in node_list]


def get_real_words(field) -> set[str]:
    all_words = get_all_words(field)
    string_words = node_list_to_str(all_words)
    return {w for w in string_words if is_world_real(w) and len(w) >= 3}

def get_max_possible_word(field) -> list[Node]:
    sorted_words = sorted(get_all_words(field), key=len)
    
    best = ""

    for word in sorted_words:
        str_word =  node_list_to_str([word, ])[0]

        starts = get_starts_with(str_word)
        ends = get_ends_with(str_word)
        

        for w in starts:
            if len(word) + 1 != len(w):
                continue
            
            
            LEFT = (word[-1].coord[0] - 1, word[-1].coord[1]) if word[-1].coord[0] != 0 else None
            RIGHT = (word[-1].coord[0] + 1, word[-1].coord[1]) if word[-1].coord[0] != 5 - 1 else None
            UP = (word[-1].coord[0], word[-1].coord[1] - 1) if word[-1].coord[1] != 0 else None
            BOTTOM = (word[-1].coord[0], word[-1].coord[1] + 1) if word[-1].coord[1] != 5 - 1 else None
            
            for side in (LEFT, RIGHT, UP, BOTTOM):
                if side:
                    if field[side[1]][side[0]] == "":
                        if len(w) > len(best):
                            best = w
                            break

        for w in ends:
            if len(word) + 1 != len(w):
                continue
            
            
            LEFT = (word[0].coord[0] - 1, word[0].coord[1]) if word[0].coord[0] != 0 else None
            RIGHT = (word[0].coord[0] + 1, word[0].coord[1]) if word[0].coord[0] != 5 - 1 else None
            UP = (word[0].coord[0], word[0].coord[1] - 1) if word[0].coord[1] != 0 else None
            BOTTOM = (word[0].coord[0], word[0].coord[1] + 1) if word[0].coord[1] != 5 - 1 else None
            
            for side in (LEFT, RIGHT, UP, BOTTOM):
                if side:
                    if field[side[1]][side[0]] == "":
                        if len(w) > len(best):
                            best = w
                            break

    return best
        
        


field = get_start_field(5)

print(get_max_possible_word(field))

print_field(field)
pprint(get_real_words(field))

