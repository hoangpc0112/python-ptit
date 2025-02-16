def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0

    return 1 if n > 1 else 0


def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    for i in a:
        for j in i:
            print(is_prime(j), end=' ')

        print()


solve()
