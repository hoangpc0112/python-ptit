def solve():
    s = input()

    while len(s) > 1:
        a = int(s[:len(s) // 2])
        b = int(s[len(s) // 2:])

        print(a + b)

        s = str(a + b)


solve()
