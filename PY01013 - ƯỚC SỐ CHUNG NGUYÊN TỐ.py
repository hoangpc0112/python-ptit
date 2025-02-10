from math import gcd


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def solve():
    a, b = map(int, input().split())
    s = str(gcd(a, b))
    tong = 0

    for char in s:
        tong += int(char)

    print("YES" if is_prime(tong) else "NO")


for i in range(int(input())):
    solve()
