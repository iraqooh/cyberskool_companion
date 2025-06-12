from typing import Tuple

def map_length(selection: str) -> Tuple:
    if selection == "short":
        return 15, 45
    elif selection == "long":
        return 80, 200
    return 30, 130