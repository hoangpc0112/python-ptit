def solve():
    n = int(input())
    sum = 0.0
    start = 1 if n & 1 else 2

    for i in range(start, n + 1, 2):
        sum += 1.0 / i

    print("{:.6f}".format(sum))


for i in range(int(input())):
    solve()
