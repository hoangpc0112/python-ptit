from math import gcd


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def solve():
    n = int(input())
    cnt = 0

    for i in range(1, n):
        if gcd(n, i) == 1:
            cnt += 1

    print("YES" if is_prime(cnt) else "NO")


t = int(input())
for i in range(t):
    solve()
