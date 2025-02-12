def backtrack(n, s, a, b, c):
    if len(s) == n:
        if a <= b and b <= c and a > 0:
            print(s)

        return

    if len(s) < n:
        backtrack(n, s + 'A', a + 1, b, c)
        backtrack(n, s + 'B', a, b + 1, c)
        backtrack(n, s + 'C', a, b, c + 1)


def solve():
    for i in range(3, int(input()) + 1):
        backtrack(i, "", 0, 0, 0)


solve()
