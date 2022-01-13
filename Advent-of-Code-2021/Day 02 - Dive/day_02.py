"""Day 02 - Dive!"""

def prepare_data(raw_data):
    """Format raw string data to objects of string and int
    and return it as a list."""
    data_list = [command.rstrip("\n").split(" ") for command in raw_data]
    data = []

    for i in data_list:
        command = {}
        command.update({"direction": i[0]})
        command.update({"value": int(i[1])})
        data.append(command)

    return data

def submarine_position(commands):
    """Return the product of final submarine x and y coordinates."""
    depth = 0
    horizontal_position = 0

    for i in commands:
        if i["direction"] == "forward":
            horizontal_position += i["value"]
        elif i["direction"] == "up":
            depth -= i["value"]
        elif i["direction"] == "down":
            depth += i["value"]

    return depth * horizontal_position

def corrected_submarine_position(commands):
    """Return the product of final submarine x and y coordinates
    calculated with corrected part two ruleset."""
    aim = 0
    depth = 0
    horizontal_position = 0

    for i in commands:
        if i["direction"] == "forward":
            horizontal_position += i["value"]
            depth += i["value"] * aim
        elif i["direction"] == "up":
            aim -= i["value"]
        elif i["direction"] == "down":
            aim += i["value"]

    return depth * horizontal_position

def main():
    """Calculate submarine positions with two different rulesets."""
    with open("test_data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = prepare_data(raw_data)

    position = submarine_position(data)
    corrected_position = corrected_submarine_position(data)

    print(f"Product of final coordinates: {position}")
    print(f"Product of correct final coordinates: {corrected_position}")

if __name__ == "__main__":
    main()
