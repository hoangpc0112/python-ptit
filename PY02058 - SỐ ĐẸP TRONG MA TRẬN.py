def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    f_max = max(max(row) for row in a)
    f_min = min(min(row) for row in a)
    gap = f_max - f_min
    found = False

    for i in range(n):
        for j in range(m):
            if a[i][j] == gap:
                found = True
                break

    if not found:
        print("NOT FOUND")
        return

    print(gap)
    for i in range(n):
        for j in range(m):
            if a[i][j] == gap:
                print(f"Vi tri [{i}][{j}]")


solve()
