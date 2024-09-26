from colorama import Fore
from typing import Literal

def set_color(color: Literal['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']) -> None:
    print(getattr(Fore, color))