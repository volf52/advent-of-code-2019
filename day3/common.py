from pathlib import Path
from typing import List, Optional, Tuple, Union, Set, Dict

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


def get_coord_lists() -> Tuple[COORDLIST, COORDLIST]:
    wire1Path, wire2Path = get_input()

    wire1Coords = path_to_visited_coords(wire1Path)
    wire2Coords = path_to_visited_coords(wire2Path)

    return wire1Coords, wire2Coords


def cross(a: COORD, b: COORD):
    return a[0] * b[1] - a[1] * b[0]


def coord_add(a: COORD, b: COORD) -> COORD:
    return (a[0] + b[0], a[1] + b[1])


def coord_sub(coordFrom: COORD, coordToSub: COORD) -> COORD:
    return (coordFrom[0] - coordToSub[0], coordFrom[1] - coordToSub[1])


def scalar_mul(coord: COORD, scalar: Union[float, int]) -> COORD:
    return (coord[0] * scalar, coord[1] * scalar)


def intersection(
        a1: COORD, a2: COORD, b1: COORD, b2: COORD
) -> Optional[COORD]:
    # https://stackoverflow.com/a/565282/4567986

    r = coord_sub(a2, a1)  # a2 - a1
    s = coord_sub(b2, b1)

    denom = cross(r, s)

    if denom == 0:
        # parallel. Not checking for collinearity, as it won't be an issue here
        return

    bma = coord_sub(b1, a1)
    u = cross(bma, r) / denom
    t = cross(bma, s) / denom

    doesIntersect = (t >= 0) and (t <= 1) and (u >= 0) and (u <= 1)
    if doesIntersect:
        x, y = coord_add(a1, scalar_mul(r, t))
        # if x > 0 and y > 0:
        return int(x), int(y)


def get_intersections(wire1Coords: COORDLIST, wire2Coords: COORDLIST) -> COORDLIST:
    intersections = []
    for i in range(1, len(wire1Coords)):
        for j in range(1, len(wire2Coords)):
            inter = intersection(wire1Coords[i - 1], wire1Coords[i], wire2Coords[j - 1], wire2Coords[j])
            if inter is not None:
                intersections.append(inter)
    return intersections


def manhattan_from_origin(c: COORD) -> int:
    x, y = c
    return abs(x) + abs(y)
