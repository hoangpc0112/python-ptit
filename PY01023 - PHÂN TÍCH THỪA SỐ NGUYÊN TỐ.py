def solve():
    n = int(input())

    if n == 1:
        print("1")
        return

    res = ""

    for i in range(2, int(n ** 0.5 + 1)):
        fre = 0

        while n % i == 0:
            fre += 1
            n //= i

        if fre > 0:
            res += str(i) + "^" + str(fre) + " * "

    if n > 1:
        res += str(n) + "^1"
    else:
        res = res[:-3]

    print("1 * " + res)


t = int(input())
for i in range(t):
    solve()
