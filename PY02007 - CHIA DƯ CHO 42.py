def solve():
    a = []

    while len(a) < 10:
        a += list(map(int, input().split()))

    for i in range(10):
        a[i] %= 42

    print(len(set(a)))


solve()
