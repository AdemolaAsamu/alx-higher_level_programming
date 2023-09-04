#!/usr/bin/python3
import sys
"""
This module runs the function that calculates the
moves on a chess board
"""


def iloc(board, row, col, n):
    """
    This checks if queen is in place
    """
    for k in range(row):
        if board[k][col] == 1:
            return False

    for k, l in range(row, -1, -1):
        l = col
        while k >= 0 and j >= 0:
            if board[k][l] == 1:
                return False
            k -= 1
            l -= 1
    
    k = row
    l = col
    while k >= 0 and l < n:
        if board[k][l] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, n):
    if row == n:
        output = []
        for k in range(n):
            row_scr = ""
            for l in range(n):
                if board[k][l] == 1:
                    row_scr += "Q"
                else:
                    row_scr += "."
            output.append(row_scr)
        return output

    results = []
    for col in range(n):
        if iloc(board, row, col, n):
            board[row][col] = 1
            result = solve_nqueens(board, row + 1, n)
            if result:
                results.extend(result)
                board[row][col] = 0


    return results

def solve(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    results = solve_nqueens(board, 0, n)
    for items in results:
        for row in results:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

        try:
            N = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        solve(N)
