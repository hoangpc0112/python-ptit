from math import gcd


def solve():
    n = int(input())
    rn = int(str(n)[::-1])
    print("YES" if gcd(n, rn) == 1 else "NO")


t = int(input())
for i in range(t):
    solve()
