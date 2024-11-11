def n_queens(n):
    col = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)
    res = []

    board = [["0"] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "1"

            backtrack(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "0"

    backtrack(0)
    return res

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solutions = n_queens(n)
    if solutions:
        print(f"\nNumber of solutions: {len(solutions)}\n")
        for sol in solutions:
            for row in sol:
                print(row)
            print()
    else:
        print("No solutions found.")
