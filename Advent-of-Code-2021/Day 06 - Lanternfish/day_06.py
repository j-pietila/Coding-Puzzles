"""Day 06 - Lanternfish"""

def get_initial_age_groups(data):
    """Return age groups with given starting point from data."""
    age_groups = {key: 0 for key in range(0, 9)}
    # Age group 6 needs to know if fish is old (resetting from 0) or new (coming from 7),
    # so new fishes don't trigger spawning before reaching 0 and resetting first.
    age_groups[6] = {"old": 0, "new": 0}

    for i in data:
        if int(i) == 6:
            age_groups[6]["old"] += 1
        else:
            age_groups[int(i)] += 1

    return age_groups

def calculate_population(age_groups):
    """Calculate and return the final population from age groups."""
    fishes = 0

    for i in age_groups:
        if i == 6:
            fishes += age_groups[i]["old"]
            fishes += age_groups[i]["new"]
        else:
            fishes += age_groups[i]

    return fishes

def population_growth(data, days):
    """Calculate and return population size from given starting
    age group data after given days."""
    age_groups = get_initial_age_groups(data)

    for _ in range(0, days):
        new_age_groups = {key: 0 for key in range(0, 9)}
        new_age_groups[6] = {"old": 0, "new": 0}

        for i in range(0, 9):
            # New age group of 5's needs both groups from 6's.
            if i == 5:
                new_age_groups[i] += age_groups[6]["old"]
                new_age_groups[i] += age_groups[6]["new"]
            # New age group of 6's come from 0's and 7's to different categories.
            elif i == 6:
                new_age_groups[i]["old"] += age_groups[0]
                new_age_groups[i]["new"] += age_groups[7]
            # New age group of 8's come from only old 6's that have come through reset.
            elif i == 8:
                new_age_groups[i] += new_age_groups[6]["old"]
            else:
                new_age_groups[i] += age_groups[i + 1]

        for j, _ in enumerate(age_groups):
            if j == 6:
                age_groups[j]["old"] = new_age_groups[j]["old"]
                age_groups[j]["new"] = new_age_groups[j]["new"]
            else:
                age_groups[j] = new_age_groups[j]

    fishes = calculate_population(age_groups)

    return fishes

def main():
    """Model the growth rate of Lanternfishes and calculate their population after given days."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = raw_data[0].split(",")

    fishes = population_growth(data, 80)

    print(f"There are {fishes} fishes after 80 days.")

    fishes2 = population_growth(data, 256)

    print(f"There are {fishes2} fishes after 256 days.")

if __name__ == "__main__":
    main()
