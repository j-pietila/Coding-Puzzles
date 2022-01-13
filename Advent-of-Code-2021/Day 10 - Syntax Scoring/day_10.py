"""Day 10 - Syntax Scoring"""

def filter_lines(lines, parentheses):
    """Return lists of corrupted and incomplete lines. Corrupted lines have
    mismatched closing parentheses, incomplete lines missing closing parentheses."""
    corrupted_lines = []
    incomplete_lines = []
    check_stack = []

    for line in lines:
        for char in line:
            if char in parentheses.values():
                check_stack.append(char)
            else:
                if parentheses.get(char) == check_stack[-1]:
                    check_stack.pop()
                else:
                    corrupted_lines.append(line)
                    check_stack.clear()
                    break

        if check_stack:
            incomplete_lines.append(line)
            check_stack.clear()

    return corrupted_lines, incomplete_lines

def check_first_corrupted_parentheses(lines, parentheses):
    """Return a list of first mismatching closing parentheses
    from every corrupted line."""
    corrupted_parentheses = []
    check_stack = []

    for line in lines:
        for char in line:
            if char in parentheses.values():
                check_stack.append(char)
            else:
                if parentheses.get(char) != check_stack.pop():
                    corrupted_parentheses.append(char)
                    check_stack.clear()
                    break

    return corrupted_parentheses

def corrupted_lines_error_score(parentheses):
    """Return total syntax error score as an integer based on
    numerical values for each corrupted parentheses."""
    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    error_score = 0

    for i in parentheses:
        error_score += values.get(i)

    return error_score

def check_missing_parentheses(lines, parentheses):
    """Return a list of lists of missing closing parentheses
    in incomplete lines."""
    missing_parentheses = []
    check_stack = []

    for line in lines:
        for char in line:
            if char in parentheses.values():
                check_stack.append(char)
            else:
                if parentheses.get(char) == check_stack[-1]:
                    check_stack.pop()

        missing_parentheses.append(check_stack.copy())
        check_stack.clear()

    return missing_parentheses

def middle_error_score(error_scores):
    """Return the middlemost error_score from given error scores.
    There are always an odd number of scores to consider."""
    middle = len(error_scores) // 2

    error_scores.sort()

    return error_scores[middle]

def incomplete_lines_error_score(parentheses):
    """Return total syntax error score as an integer based on calculations
    with numerical values for each incomplete lines parentheses. Total
    syntax error is the middlemost error score from all the lines."""
    values = {"(": 1, "[": 2, "{": 3, "<": 4}
    error_scores = []

    for line in parentheses:
        line.reverse()
        error_score = 0

        for parenthese in line:
            error_score *= 5
            error_score += values.get(parenthese)

        error_scores.append(error_score)

    error_score = middle_error_score(error_scores)

    return error_score

def main():
    """Calculate syntax error scores for corrupted and
    incomplete lines in submarine navigation subsystem."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    data = [i.rstrip("\n") for i in raw_data]

    correct_parentheses = {")": "(", "]": "[", "}": "{", ">": "<"}

    corrupted_lines, incomplete_lines = filter_lines(data, correct_parentheses)

    corrupted_parentheses = check_first_corrupted_parentheses(corrupted_lines, correct_parentheses)

    corrupted_error_score = corrupted_lines_error_score(corrupted_parentheses)

    print(f"Total syntax error score for corrupted lines: {corrupted_error_score}")

    missing_parentheses = check_missing_parentheses(incomplete_lines, correct_parentheses)

    incomplete_error_score = incomplete_lines_error_score(missing_parentheses)

    print(f"Total syntax error score for incomplete lines: {incomplete_error_score}")

if __name__ == "__main__":
    main()
