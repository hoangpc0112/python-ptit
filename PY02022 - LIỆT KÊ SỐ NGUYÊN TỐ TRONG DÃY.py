def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return n > 1


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    f = [0] * (10**6 + 1)

    for i in a:
        if is_prime(int(i)):
            f[int(i)] += 1

    for i in a:
        if f[i] > 0:
            print(i, f[i])
            f[i] = 0


solve()
