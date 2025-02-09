def solve():
    n = int(input())

    if n <= 10:
        print(n)
        return

    pow = 10
    res = n

    while res > pow:
        digit = (res // (pow // 10)) % 10

        if digit >= 5:
            res = ((res // pow) + 1) * pow
        else:
            res = (res // pow) * pow

        pow *= 10

    print(res)


t = int(input())
for i in range(t):
    solve()
