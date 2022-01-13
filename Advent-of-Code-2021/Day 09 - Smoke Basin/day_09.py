"""Day 09 - Smoke Basin"""

def check_adjacent_points(cave_floor, point):
    """Return list of points that are adjacent to given point straight up,
    down, left or right as [(x, y), value]."""
    adjacent_points = []
    row, col = point

    if row != 0:
        adjacent_points.append([(row - 1, col), cave_floor[row - 1][col]])
    if row + 1 != len(cave_floor):
        adjacent_points.append([(row + 1, col), cave_floor[row + 1][col]])
    if col != 0:
        adjacent_points.append([(row, col - 1), cave_floor[row][col - 1]])
    if col + 1 != len(cave_floor[row]):
        adjacent_points.append([(row, col + 1), cave_floor[row][col + 1]])

    return adjacent_points

def check_low_points(cave_floor):
    """Return list of low points from cave floor as [(x, y), value].
    Low point is a point where all adjacent points up, down, left and right
    from it are lower than itself."""
    low_points = []

    for row, i in enumerate(cave_floor):
        for col, point in enumerate(i):
            adjacent_points = check_adjacent_points(cave_floor, (row, col))
            adjacent_values = [i[1] for i in adjacent_points]

            if all(val > point for val in adjacent_values):
                low_points.append([(row, col), point])

    return low_points

def calculate_risk_level(low_points):
    """Return total risk level as an integer by adding one to each low point
    value and summing them together."""
    total_risk = 0

    for i in low_points:
        total_risk += i[1] + 1

    return total_risk

def map_single_basin(cave_floor, low_point):
    """Return (x,y) coordinates of all points in a single basin
    originating from a given low_point."""
    basin_points = [low_point[0]]

    first_points = check_adjacent_points(cave_floor, low_point[0])
    current_points = [{"points": first_points, "prev_val": low_point[1]}]
    next_points = set()

    while current_points:
        for i in current_points:
            points = i.get("points")
            previous_val = i.get("prev_val")
            for point in points:
                if point[1] > previous_val and point[1] < 9:
                    next_points.add(point[0])

        current_points.clear()

        if next_points:
            for point in next_points:
                row, col = point
                adjacent_points = check_adjacent_points(cave_floor, point)
                current_points.append({"points": adjacent_points, "prev_val": cave_floor[row][col]})

        basin_points += list(next_points)
        next_points.clear()

    return len(set(basin_points))

def calculate_final_basin_size(basin_sizes):
    """Return the product of three largest basin sizes as the final
    basin size answer."""
    basin_sizes.sort()
    largest_basins = basin_sizes[-3:]

    final_basin_size = 1

    for i in largest_basins:
        final_basin_size *= i

    return final_basin_size

def main():
    """Determine the low points and risk level of the ocean floor
    and calculate the final basin size based on three largest basins."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = [i.rstrip("\n") for i in raw_data]
    data = [[int(j) for j in i] for i in data]

    low_points = check_low_points(data)

    risk_level = calculate_risk_level(low_points)

    print(f"Total risk level is {risk_level}")

    basin_sizes = []

    for i in low_points:
        basin_size = map_single_basin(data, i)
        basin_sizes.append(basin_size)

    final_basin_size = calculate_final_basin_size(basin_sizes)

    print(f"Final basin size: {final_basin_size}")

if __name__ == "__main__":
    main()
