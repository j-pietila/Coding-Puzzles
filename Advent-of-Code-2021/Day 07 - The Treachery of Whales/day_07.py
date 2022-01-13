"""Day 07 - The Treachery of Whales"""

def calculate_possible_positions(submarine_positions):
    """Return list of possible optimal positions between the lowest and
    highest submarine position."""
    lowest_pos = submarine_positions[0]
    highest_pos = submarine_positions[-1]

    possible_positions = [i for i in range(lowest_pos, highest_pos + 1)]

    return possible_positions

def calculate_distances(submarine_positions, possible_positions):
    """Return distances of submarine positions from each possible optimal position."""
    fuel_costs = {}

    for i in possible_positions:
        moves = []
        for j in submarine_positions:
            distance = abs(j - i)
            moves.append(distance)

        fuel_costs[i] = moves

    return fuel_costs

def fuel_cost_from_moves(submarine_positions, possible_positions):
    """Return dictionary of moves needed for each possible position."""
    fuel_costs = {}

    for i in possible_positions:
        fuel_costs[i] = 0
        for j in submarine_positions:
            fuel_costs[i] += abs(j - i)

    return fuel_costs

def fuel_cost_from_distances(distances):
    """Return dictionary of fuel costs for each possible position calculated
    as sum of natural numbers from list of distances."""
    fuel_costs = {}
    positions = list(distances.keys())

    for i in positions:
        total_distance = 0
        moves = distances[i]
        for j in moves:
            total_distance += (j * (j + 1)) / 2
        fuel_costs[i] = total_distance

    return fuel_costs

def main():
    """Calculate the optimal horizontal positions for crab submarines."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = raw_data[0].split(",")

    submarine_positions = [int(i) for i in data]
    submarine_positions.sort()

    possible_positions = calculate_possible_positions(submarine_positions)

    fuel_costs = fuel_cost_from_moves(submarine_positions, possible_positions)

    optimal_position = min(fuel_costs, key=fuel_costs.get)

    print(f"Optimal position: {optimal_position} with {fuel_costs.get(optimal_position)} fuel")

    distances_per_position = calculate_distances(submarine_positions, possible_positions)

    fuel_costs = fuel_cost_from_distances(distances_per_position)

    optimal_position = min(fuel_costs, key=fuel_costs.get)

    print(f"Updated optimal position: {optimal_position} with {int(fuel_costs.get(optimal_position))} fuel")

if __name__ == "__main__":
    main()
