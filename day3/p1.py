from day3.common import (
    get_coord_lists,
    get_intersections,
    manhattan_from_origin,
    path_to_visited_coords
)

wire1Path = ''.split(',')
wire2Path = ''.split(',')

wire1Coords = path_to_visited_coords(wire1Path)
wire2Coords = path_to_visited_coords(wire2Path)
# wire1Coords, wire2Coords = get_coord_lists()
intersections = get_intersections(wire1Coords, wire2Coords)

min_coord = min(intersections, key=manhattan_from_origin)

print(wire1Coords)
print(wire2Coords)
print(intersections)

print(min_coord)
print(manhattan_from_origin(min_coord))
