"""
N-queens in Python (find ways to fit N queens on an N*N chessboard such that no
queen can target another queen. Prints all valid boards for a given number n.
"""

import argparse

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", type=int, default=8, help="The size of the board")
    return parser.parse_args()

# check if no queens share a column
def cols_valid(positions, target):
    return len(set(positions)) == target

# these two functions use a little bit of mathematical reasoning - if a queen
# at (x, y) is shifted along one diagonal, it arrives can arrive at one of:
# (x + shift, y + shift), in which case (x - y) remains constant, or
# (x - shift, y + shift), in which case (x + y) remains constant.

# check if no queens share a diagonal one way
def diag_valid_a(positions, target):
    return len(set(a - b for a, b in positions)) == target

# check the other way
def diag_valid_b(positions, target):
    return len(set(a + b for a, b in positions)) == target

def is_valid(positions):
    filtered = [i for i in positions if i is not None]
    ind_filtered = [(ind, i) for ind, i in enumerate(positions) if i is not None]
    target = len(filtered)

    return (cols_valid(filtered, target) and
            diag_valid_a(ind_filtered, target) and
            diag_valid_b(ind_filtered, target))

def print_positions(positions):
    for ind, pos in enumerate(positions):
        row = ["_"] * len(positions)

        if pos is not None:
            row[pos] = "Q"
        
        print(" ".join(row))

# gotcha: it only yields a reference to a list that will itself change as soon
# as the generator continues. If you want to store a copy of all solutions,
# explicitly perform a copy (as it's a one-dimensional list, positions[:]
# should suffice)
def _n_queens(positions, n, ind):
    if ind == n:
        yield positions
    else:
        for i in range(n):
            positions[ind] = i
            if is_valid(positions):
                yield from _n_queens(positions, n, ind + 1)

            positions[ind] = None

def n_queens(n):
    yield from _n_queens([None] * n, n, 0)

def main():
    args = get_args()

    for ind, board in enumerate(n_queens(args.n)):
        print("Board {}:".format(ind))
        print_positions(board)

if __name__ == "__main__":
    main()
