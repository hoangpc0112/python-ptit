def solve():
    while True:
        n = int(input())

        if n == 0:
            return

        if n == 1:
            print('1')
            continue

        res = 0

        while n > 1:
            if n & 1:
                n = n * 3 + 1
            else:
                n //= 2

            res += 1

        print(res + 1)


solve()
