from pathlib import Path
from typing import Dict, Generator, List, Set, Tuple

COORD = Tuple[int, int]
NODELIST = Dict[COORD, int]


def get_input() -> Tuple[List[str], List[str]]:
    pth = Path(__file__).parent.joinpath("input")
    splt = pth.read_text().splitlines()
    assert len(splt) == 2
    wire1Path = splt[0].split(",")
    wire2Path = splt[1].split(",")

    return wire1Path, wire2Path


def update_steps(visited: NODELIST, c: COORD, steps: int) -> None:
    prev = visited.get(c)
    if prev is None:
        visited[c] = steps


def path_to_visited_coords(path: List[str]) -> NODELIST:
    x = 0
    y = 0
    steps = 0
    visited: NODELIST = {}
    for move in path:
        direction = move[0]
        displacement = int(move[1:])
        if direction == "R":
            for _ in range(displacement):
                x += 1
                steps += 1
                update_steps(visited, (x, y), steps)
        elif direction == "L":
            for _ in range(displacement):
                x -= 1
                steps += 1
                update_steps(visited, (x, y), steps)
        elif direction == "U":
            for _ in range(displacement):
                y += 1
                steps += 1
                update_steps(visited, (x, y), steps)
        elif direction == "D":
            for _ in range(displacement):
                y -= 1
                steps += 1
                update_steps(visited, (x, y), steps)
        else:
            raise ValueError(f"Invalid direction: {direction}")

    return visited


def get_visited_coords() -> Tuple[NODELIST, NODELIST]:
    wire1Path, wire2Path = get_input()

    wire1Coords = path_to_visited_coords(wire1Path)
    wire2Coords = path_to_visited_coords(wire2Path)

    return wire1Coords, wire2Coords


def get_intersections(
        wire1Coords: NODELIST, wire2Coords: NODELIST
) -> Set[COORD]:
    return set(wire1Coords.keys()).intersection(wire2Coords.keys())


def get_step_list(
        wire1Coords: NODELIST, wire2Coords: NODELIST
) -> Generator[int, None, None]:
    common_keys = get_intersections(wire1Coords, wire2Coords)
    return (wire1Coords[k] + wire2Coords[k] for k in common_keys)


def manhattan_from_origin(c: COORD) -> int:
    x, y = c
    return abs(x) + abs(y)
