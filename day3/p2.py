from day3.common import get_step_list, get_visited_coords

wire1Coords, wire2Coords = get_visited_coords()

step_list_generator = get_step_list(wire1Coords, wire2Coords)
minSteps = min(step_list_generator)

print(minSteps)
