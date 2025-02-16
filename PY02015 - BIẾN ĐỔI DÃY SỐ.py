def solve():
    while True:
        a = list(map(int, input().split()))

        if a == [0, 0, 0, 0]:
            return

        res = 0

        while len(set(a)) != 1:
            b = []

            for i in range(4):
                b.append(abs(a[i] - a[(i + 1) % 4]))

            a = b
            res += 1

        print(res)


solve()
