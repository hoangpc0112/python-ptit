def get_score(value):
    if value < 5:
        return 2.5
    elif value < 7:
        return 3.0
    elif value < 10:
        return 3.5
    elif value < 13:
        return 4.0
    elif value < 16:
        return 4.5
    elif value < 20:
        return 5.0
    elif value < 23:
        return 5.5
    elif value < 27:
        return 6.0
    elif value < 30:
        return 6.5
    elif value < 33:
        return 7.0
    elif value < 35:
        return 7.5
    elif value < 37:
        return 8.0
    elif value < 39:
        return 8.5
    return 9.0


def solve():
    a, b, c, d = map(float, input().split())

    a = get_score(a)
    b = get_score(b)

    total = (a + b + c + d) / 4

    if 0.25 <= total % 1 < 0.75:
        total = int(total) + 0.5
    elif 0.75 <= total % 1:
        total = int(total) + 1
    else:
        total = int(total)

    print(f"{total:.1f}")


for i in range(int(input())):
    solve()
