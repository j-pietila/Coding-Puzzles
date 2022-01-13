"""Day 04 - Giant Squid"""

def get_boards(raw_data):
    """Extract separate boards from raw data stream."""
    boards = []

    # By using step 6 with i and adding 0-4 to i with j, we can skip every 6th line
    # separating different boards with an empty line.
    for i in range(2, len(raw_data), 6):
        board = []

        for j in range(0, 5):
            board += raw_data[i + j].rstrip("\n").split(" ")

        # Splitting works but gives empty terms as numbers below 10 have additional empty space
        # in front of them. These just need to be filtered out.
        board = filter(lambda num: num != "", board)
        boards.append(list(board))

    return boards

def format_boards(boards):
    """Format boards so that each number term is converted to a dictionary
    with 'number' and 'marked' key-value pairs."""
    for board in boards:
        for i, val in enumerate(board):
            board[i] = {"number": val, "marked": 0}

def print_boards(boards):
    """Testing function: Print given boards in 5x5 format to console."""
    for i in boards:
        for j, val in enumerate(i):
            if (j + 1) % 5 != 0:
                print(val, end=" ")
            else:
                print(val, end="\n")
        print()

def mark_boards(bingo_num, boards):
    """Mark given bingo number in each board if found."""
    for i in boards:
        marked_num = next((num for num in i if num["number"] == bingo_num), None)
        if marked_num:
            marked_num["marked"] = 1

def check_boards(boards):
    """Check board rows and columns for bingo wins."""
    winning_boards = []

    for i, board in enumerate(boards):
        rows = check_rows(board)
        columns = check_columns(board)

        if rows or columns:
            winning_boards.append({"index": i, "board": board})

    return winning_boards

def check_rows(board):
    """Check every row in board for bingo win."""
    for i in range(0, len(board), 5):
        marks = 0

        for j in range(0, 5):
            if board[i + j].get("marked") == 1:
                marks += 1

        if marks == 5:
            return True

    return None

def check_columns(board):
    """Check every column in board for bingo win."""
    for i in range(0, 5):
        marks = 0

        for j in range(0, len(board), 5):
            if board[i + j].get("marked") == 1:
                marks += 1

        if marks == 5:
            return True

    return None

def winning_score(num, board):
    """Calculate winning score by multiplying sum of unmarked numbers in winning bingo
    board by the last bingo number drawn."""
    unmarked_sum = 0

    for i in board:
        if i.get("marked") == 0:
            unmarked_sum += int(i.get("number"))

    return unmarked_sum * int(num)

def first_win_board_score(raw_data):
    """Calculate winning score of the bingo board first to win."""
    bingo_numbers = raw_data[0].rstrip("\n").split(",")
    boards = get_boards(raw_data)

    format_boards(boards)

    for i in bingo_numbers:
        mark_boards(i, boards)
        winning_board = check_boards(boards)

        if winning_board:
            score = winning_score(i, winning_board[0].get("board"))
            return score

    return None

def last_win_board_score(raw_data):
    """Calculate winning score of the bingo board last to win."""
    bingo_numbers = raw_data[0].rstrip("\n").split(",")
    boards = get_boards(raw_data)

    format_boards(boards)

    for i in bingo_numbers:
        mark_boards(i, boards)
        winning_boards = check_boards(boards)

        if len(boards) > 1 and winning_boards:
            # Need to loop from end to beginning to pop multiple indexes correctly.
            for board in reversed(winning_boards):
                boards.pop(board.get("index"))
        elif len(boards) == 1 and winning_boards:
            score = winning_score(i, winning_boards[0].get("board"))
            return score

    return None

def main():
    """Draw the bingo numbers, mark bingo boards, check winning board and calculate
    the winning score."""
    with open("data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    first_to_win_score = first_win_board_score(raw_data)

    print(f"Final score of the board to win first is: {first_to_win_score}")

    last_to_win_score = last_win_board_score(raw_data)

    print(f"Final score of the board to win last is: {last_to_win_score}")

if __name__ == "__main__":
    main()
