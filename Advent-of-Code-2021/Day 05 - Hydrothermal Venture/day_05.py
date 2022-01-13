"""Day 05 - Hydrothermal Venture"""

def get_coordinates(data):
    """Extract and return coordinates as list of dictionaries from data."""
    straight_coordinates = []
    diagonal_coordinates = []

    for i, val in enumerate(data):
        data[i] = val[0].split(",") + val[1].split(",")
        coordinate = {
            "x1": int(data[i][0]),
            "y1": int(data[i][1]),
            "x2": int(data[i][2]),
            "y2": int(data[i][3])
        }

        if (coordinate.get("x1") == coordinate.get("x2") or
            coordinate.get("y1") == coordinate.get("y2")):
            straight_coordinates.append(coordinate)
        else:
            diagonal_coordinates.append(coordinate)


    return straight_coordinates, diagonal_coordinates

def get_max_coordinates(coordinates):
    """Return max values for x and y in coordinates"""
    max_x = 0
    max_y = 0

    for i in coordinates:
        for j in i:
            if j.get("x1") > max_x:
                max_x = j.get("x1")
            if j.get("x2") > max_x:
                max_x = j.get("x2")
            if j.get("y1") > max_y:
                max_y = j.get("y1")
            if j.get("y2") > max_y:
                max_y = j.get("y2")

    return max_x, max_y

def generate_map(max_coordinates):
    """Generate list representing the ocean floor based on max coordinates."""
    max_x = max_coordinates[0] + 1
    max_y = max_coordinates[1] + 1

    ocean_floor_map = [[0 for i in range(0, max_x)] for j in range(0, max_y)]

    return ocean_floor_map

def print_map(ocean_floor):
    """Testing function: Print given map to console."""
    for i, row in enumerate(ocean_floor):
        print(i, row)


def map_coordinate_points_straight(coordinates):
    """Map all the coordinate points between straight line end points."""
    coordinate_points = []

    if coordinates.get("x1") == coordinates.get("x2"):
        if coordinates.get("y1") > coordinates.get("y2"):
            min_y, max_y = coordinates.get("y2"), coordinates.get("y1")
        else:
            min_y, max_y = coordinates.get("y1"), coordinates.get("y2")

        for i in range(min_y, max_y + 1):
            coordinate_points.append({"x": coordinates.get("x1"), "y": i})
    else:
        if coordinates.get("x1") > coordinates.get("x2"):
            min_x, max_x = coordinates.get("x2"), coordinates.get("x1")
        else:
            min_x, max_x = coordinates.get("x1"), coordinates.get("x2")

        for i in range(min_x, max_x + 1):
            coordinate_points.append({"x": i, "y": coordinates.get("y1")})

    return coordinate_points

def map_coordinate_points_diagonal(coordinates):
    """Map all the coordinate points between diagonal line end points."""
    coordinate_points = []

    for i in range(0, abs(coordinates.get("x1") - coordinates.get("x2")) + 1):
        if coordinates.get("x1") < coordinates.get("x2"):
            x_val = coordinates.get("x1") + i
        else:
            x_val = coordinates.get("x1") - i
        if coordinates.get("y1") < coordinates.get("y2"):
            y_val = coordinates.get("y1") + i
        else:
            y_val = coordinates.get("y1") - i

        coordinate_points.append({"x": x_val, "y": y_val})

    return coordinate_points

def mark_points_to_map(ocean_floor, coordinate_points):
    """Mark given coordinate points to map."""
    for i in coordinate_points:
        ocean_floor[i.get("y")][i.get("x")] += 1

def calculate_dangerous_points(ocean_floor):
    """Return amount of dangerous points having at least two crossing lines."""
    dangerous_points = [(row, col) for row in ocean_floor for col in row if col >= 2]

    return len(dangerous_points)

def map_dangerous_areas(raw_data):
    """Calculate dangerous points from straight lines."""
    data = [line.rstrip("\n").split(" -> ") for line in raw_data]

    coordinates = get_coordinates(data)
    straight_coordinates = coordinates[0]

    ocean_floor = generate_map(get_max_coordinates(coordinates))

    for i in straight_coordinates:
        coordinate_points = map_coordinate_points_straight(i)
        mark_points_to_map(ocean_floor, coordinate_points)

    dangerous_points = calculate_dangerous_points(ocean_floor)

    return dangerous_points

def map_dangerous_areas_diagonal(raw_data):
    """Calculate dangerous points from straight and diagonal lines."""
    data = [line.rstrip("\n").split(" -> ") for line in raw_data]

    coordinates = get_coordinates(data)
    straight_coordinates = coordinates[0]
    diagonal_coordinates = coordinates[1]

    ocean_floor = generate_map(get_max_coordinates(coordinates))

    for i in straight_coordinates:
        coordinate_points = map_coordinate_points_straight(i)
        mark_points_to_map(ocean_floor, coordinate_points)

    for i in diagonal_coordinates:
        coordinate_points = map_coordinate_points_diagonal(i)
        mark_points_to_map(ocean_floor, coordinate_points)

    dangerous_points = calculate_dangerous_points(ocean_floor)

    return dangerous_points

def main():
    """Calculate dangerous spots on the ocean floor with given coordinate points."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    dangerous_points = map_dangerous_areas(raw_data)

    print(f"There are {dangerous_points} dangerous points on the ocean floor with straight lines.")

    dangerous_points_diagonal = map_dangerous_areas_diagonal(raw_data)

    print(f"There are {dangerous_points_diagonal} dangerous points on the ocean floor " +
           "with straight and diagonal lines.")

if __name__ == "__main__":
    main()
