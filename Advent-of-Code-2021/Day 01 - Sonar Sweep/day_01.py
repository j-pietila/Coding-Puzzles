"""Day 01 - Sonar Sweep"""

def simple_sonar_analysis(readings):
    """Return the number of times a depth measurement increases."""
    depth_increases = 0

    for i in range(1, len(readings)):
        if readings[i] > readings[i - 1]:
            depth_increases += 1

    return depth_increases

def advanced_sonar_analysis(readings):
    """Return the number of times a depth measurement between
    three-measurement sliding windows increases."""
    three_measurement_windows = []

    for i in range(0, len(readings) - 2):
        window = readings[i] + readings[i + 1] + readings[i + 2]
        three_measurement_windows.append(window)

    depth_increases = simple_sonar_analysis(three_measurement_windows)

    return depth_increases

def main():
    """Run simple and advanced sonar analyses."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = [int(line.rstrip("\n")) for line in raw_data]

    simple_analysis = simple_sonar_analysis(data)
    advanced_analysis = advanced_sonar_analysis(data)

    print(f"Simple sonar analysis: {simple_analysis} increases in depth.")
    print(f"Advanced sonar analysis: {advanced_analysis} increases in depth.")

if __name__ == "__main__":
    main()
