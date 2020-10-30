from pathlib import Path
from typing import Dict, List, Set, Tuple

COORD = Tuple[int, int]
COORDLIST = Set[COORD]


def get_input() -> Tuple[List[str], List[str]]:
    pth = Path(__file__).parent.joinpath("input")
    splt = pth.read_text().splitlines()
    assert len(splt) == 2
    wire1Path = splt[0].split(",")
    wire2Path = splt[1].split(",")

    return wire1Path, wire2Path


def path_to_visited_coords(path: List[str]) -> COORDLIST:
    x = 0
    y = 0
    visited: Dict[COORD, bool] = {}
    for move in path:
        direction = move[0]
        displacement = int(move[1:])
        if direction == "R":
            for _ in range(displacement):
                x += 1
                visited[(x, y)] = True
        elif direction == "L":
            for _ in range(displacement):
                x -= 1
                visited[(x, y)] = True
        elif direction == "U":
            for _ in range(displacement):
                y += 1
                visited[(x, y)] = True
        elif direction == "D":
            for _ in range(displacement):
                y -= 1
                visited[(x, y)] = True
        else:
            raise ValueError(f"Invalid direction: {direction}")

    return set(visited.keys())


def get_visited_coords() -> Tuple[COORDLIST, COORDLIST]:
    wire1Path, wire2Path = get_input()

    wire1Coords = path_to_visited_coords(wire1Path)
    wire2Coords = path_to_visited_coords(wire2Path)

    return wire1Coords, wire2Coords


def manhattan_from_origin(c: COORD) -> int:
    x, y = c
    return abs(x) + abs(y)
