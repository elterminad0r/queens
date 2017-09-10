# queens
The n-queens problem in Python. A command-line script to generate all solutions to the problem for an n\*n chessboard (the problem being to fit n queens on this board such that no queen can target another). It uses the relatively naive backtracking technique. It stores queens as a list of length `n`, where each element is the `y`-coordinate of a queen (or `None`) if the queen doesn't exist.

The default case is 8\*8 - so calling with `$ python queens.py` results in something like this:

    Board 0:
    Q _ _ _ _ _ _ _
    _ _ _ _ Q _ _ _
    _ _ _ _ _ _ _ Q
    _ _ _ _ _ Q _ _
    _ _ Q _ _ _ _ _
    _ _ _ _ _ _ Q _
    _ Q _ _ _ _ _ _
    _ _ _ Q _ _ _ _
    Board 1:
    Q _ _ _ _ _ _ _
    _ _ _ _ _ Q _ _
    _ _ _ _ _ _ _ Q
    _ _ Q _ _ _ _ _
    _ _ _ _ _ _ Q _
    _ _ _ Q _ _ _ _
    _ Q _ _ _ _ _ _
    _ _ _ _ Q _ _ _

    ...

    Board 91:
    _ _ _ _ _ _ _ Q
    _ _ _ Q _ _ _ _
    Q _ _ _ _ _ _ _
    _ _ Q _ _ _ _ _
    _ _ _ _ _ Q _ _
    _ Q _ _ _ _ _ _
    _ _ _ _ _ _ Q _
    _ _ _ _ Q _ _ _

It works for any board dimension - eg `$ python -n 13`.

It features a little optimisation - minimising dual computation and reconstruction of objects - `positions` in `_n_queens` is always the same list, and its length is never changed.
