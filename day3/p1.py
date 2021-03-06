from day3.common import (
    get_intersections,
    get_visited_coords,
    manhattan_from_origin,
)

wire1Coords, wire2Coords = get_visited_coords()
intersections = get_intersections(wire1Coords, wire2Coords)

min_coord = min(intersections, key=manhattan_from_origin)

# print(wire1Coords)
# print(wire2Coords)
print(intersections)

print(min_coord)
print(manhattan_from_origin(min_coord))
