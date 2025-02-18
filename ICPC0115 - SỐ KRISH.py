from math import factorial


def solve():
    n = input()
    print("Yes" if sum(factorial(int(i)) for i in n) == int(n) else "No")


for i in range(int(input())):
    solve()
