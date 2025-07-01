from collections.abc import Sequence
import re
import random

with open("./src/sources/russian.txt") as words_file:
    source_words = words_file.read().upper()


def get_starts_with(letters: str) -> Sequence[str]:
    return re.findall(f"^{letters}.*$", source_words, re.MULTILINE)

def get_ends_with(letters: str) -> Sequence[str]:
    return re.findall(f"^.*{letters}$", source_words, re.MULTILINE)


def get_random(size: int = 5) -> str:
    return random.choice(re.findall(f"^{'.'*size}$", source_words, re.MULTILINE))

def is_world_real(word: str) -> bool:
    return f"\n{word}\n" in source_words





