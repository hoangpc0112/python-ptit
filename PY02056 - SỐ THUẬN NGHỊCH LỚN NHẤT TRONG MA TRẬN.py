def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    f_max = 0

    for i in range(n):
        for j in range(m):
            if a[i][j] >= 10 and str(a[i][j]) == str(a[i][j])[::-1] and a[i][j] > f_max:
                f_max = a[i][j]

    if f_max == 0:
        print("NOT FOUND")
        return

    print(f_max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == f_max:
                print(f"Vi tri [{i}][{j}]")


solve()
