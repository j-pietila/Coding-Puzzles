"""Day 03 - Binary Diagnostic"""

def calculate_bits(diagnostic):
    """Calculate bits by position in the diagnostic bit sequence."""
    diagnostic_bits = []

    for i in range(0, len(diagnostic[0])):
        bits = {0: 0, 1: 0}
        for j in diagnostic:
            if j[i] == "0":
                bits[0] += 1
            else:
                bits[1] += 1

        diagnostic_bits.append(bits)

    return diagnostic_bits

def calculate_bit(diagnostic, index):
    """Calculate bits by given position in diagnostic bit sequence."""
    diagnostic_bit = {0: 0, 1: 0}

    for i in diagnostic:
        if i[index] == "0":
            diagnostic_bit[0] += 1
        else:
            diagnostic_bit[1] += 1

    return diagnostic_bit

def determine_gamma_rate(diagnostic_bits):
    """Return gamma rate as a string by determining the most
    common bit in each position of diagnostic bit sequences."""
    gamma_rate = "".join("0" if bit[0] > bit[1] else "1" for bit in diagnostic_bits)

    return gamma_rate

def determine_epsilon_rate(gamma_rate):
    """Return epsilon rate as a string by determining it from
    gamma rate by inverting every bit in it."""
    epsilon_rate = "".join("0" if bit == "1" else "1" for bit in gamma_rate)

    return epsilon_rate

def oxygen_generator_and_scrubber_rates(diagnostic):
    """Determine oxygen generator and scrubber rates by determining the most
    common bits in each position of diagnostic bit sequences, and filtering
    out sequences that differ from that accordingly."""
    oxygen_generator_rate = diagnostic.copy()
    scrubber_rate = diagnostic.copy()

    for i in range(0, len(diagnostic[0])):
        diagnostic_bit_oxygen = calculate_bit(oxygen_generator_rate, i)
        diagnostic_bit_scrubber = calculate_bit(scrubber_rate, i)

        oxygen_bit = "".join(
            "1" if diagnostic_bit_oxygen[1] >= diagnostic_bit_oxygen[0] else "0")
        scrubber_bit = "".join(
            "0" if diagnostic_bit_scrubber[0] <= diagnostic_bit_scrubber[1] else "1")

        if len(oxygen_generator_rate) > 1:
            filtered_oxygen_rating = filter(
                lambda bit: bit[i] == oxygen_bit, oxygen_generator_rate)
            oxygen_generator_rate = list(filtered_oxygen_rating)
        if len(scrubber_rate) > 1:
            filtered_scrubber_rate = filter(
                lambda bit: bit[i] == scrubber_bit, scrubber_rate)
            scrubber_rate = list(filtered_scrubber_rate)

    return oxygen_generator_rate[0], scrubber_rate[0]


def main():
    """Determine the power consumption and life support rating
    of the submarine."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = [line.rstrip("\n") for line in raw_data]

    gamma_rate = determine_gamma_rate(calculate_bits(data))
    epsilon_rate = determine_epsilon_rate(gamma_rate)

    print(f"Power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")

    oxygen_generator_rate, scrubber_rate = oxygen_generator_and_scrubber_rates(data)

    print(f"Life support rating: {int(oxygen_generator_rate, 2) * int(scrubber_rate, 2)}")

if __name__ == "__main__":
    main()
