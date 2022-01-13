"""Day 08 - Seven Segment Search"""

def count_unique_digits(data):
    """Return number of unique digits in data outputs."""
    unique_digits = 0
    unique_digit_lengths = [2, 3, 4, 7]
    output = [i.split(" | ") for i in data]
    output_values = [i[1] for i in output]

    for i in output_values:
        digits = i.split(" ")
        for j in digits:
            if (len(j) in unique_digit_lengths):
                unique_digits += 1

    return unique_digits

def matches(a, b):
    """Return number of matching letters found between strings a and b."""
    matches = 0

    for i in a:
        if i in b:
            matches += 1

    return matches

def decode_digits(data):
    """Return dictionary of digits and their signals for given display."""
    digits = {key: "" for key in range(0, 10)}

    display = data.split(" ")
    display = ["".join(sorted(i)) for i in display]

    one = [i for i in display if len(i) == 2]
    digits[1] = display.pop(display.index(one[0]))

    four = [i for i in display if len(i) == 4]
    digits[4] = display.pop(display.index(four[0]))

    seven = [i for i in display if len(i) == 3]
    digits[7] = display.pop(display.index(seven[0]))

    eight = [i for i in display if len(i) == 7]
    digits[8] = display.pop(display.index(eight[0]))

    three = [i for i in display if (len(i) == 5 and matches(one[0], i) == 2)]
    digits[3] = display.pop(display.index(three[0]))

    two = [i for i in display if (len(i) == 5 and matches(four[0], i) == 2)]
    digits[2] = display.pop(display.index(two[0]))

    five = [i for i in display if len(i) == 5]
    digits[5] = display.pop(display.index(five[0]))

    six = [i for i in display if (len(i) == 6 and matches(one[0], i) == 1)]
    digits[6] = display.pop(display.index(six[0]))

    nine = [i for i in display if (len(i) == 6 and matches(four[0], i) == 4)]
    digits[9] = display.pop(display.index(nine[0]))

    zero = [i for i in display if len(i) == 6]
    digits[0] = display.pop(display.index(zero[0]))

    return digits

def decode_single_output(display):
    """Return decoded output of given display as an integer."""
    decoded_display = decode_digits(display[0])
    output = display[1].split(" ")
    output = ["".join(sorted(i)) for i in output]
    decoded_output = ""

    key_list = list(decoded_display.keys())
    val_list = list(decoded_display.values())

    for i in output:
        index = val_list.index(i)
        decoded_output += str(key_list[index])

    return int(decoded_output)

def decode_outputs(data):
    """Return list of decoded integer outputs for every display in data."""
    displays = [i.split(" | ") for i in data]
    decoded_outputs = []
    
    for i in displays:
        decoded_outputs.append(decode_single_output(i))

    return decoded_outputs

def calculate_total_output(outputs):
    """Return sum of all given decoded outputs."""
    total_output = 0

    for i in outputs:
        total_output += i

    return total_output

def main():
    """Decode the scrambled signals."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = [i.rstrip("\n") for i in raw_data]

    unique_digits = count_unique_digits(data)

    print(f"There are {unique_digits} unique digits in undecoded displays")

    decoded_outputs = decode_outputs(data)

    total_output = calculate_total_output(decoded_outputs)

    print(f"Total output of all decoded displays is {total_output}")

if __name__ == "__main__":
    main()
