def backtrack(n, a, b, c):
    if n == 1:
        print(a + " -> " + c)
        return

    backtrack(n - 1, a, c, b)
    backtrack(1, a, b, c)
    backtrack(n - 1, b, a, c)


def solve():
    backtrack(int(input()), "A", "B", "C")


solve()
