def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return n > 1


def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    f_max = 0

    for i in range(n):
        for j in range(m):
            if is_prime(a[i][j]) and a[i][j] > f_max:
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
