from math import sqrt

data = []
start = 0


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def solve():
    global start

    a = distance(data[start], data[start + 1],
                 data[start + 2], data[start + 3])

    b = distance(data[start + 2], data[start + 3],
                 data[start + 4], data[start + 5])

    c = distance(data[start + 4], data[start + 5],
                 data[start], data[start + 1])

    if max([a, b, c]) * 2 >= a + b + c:
        print("INVALID")
    else:
        print(f"{a + b + c:.3f}")

    start += 6


t = int(input())

while True:
    try:
        data += list(map(float, input().split()))
    except Exception:
        break

for i in range(t):
    solve()
