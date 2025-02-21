def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    print(max(a[-1] * a[-2] * a[-3], a[0] * a[1]
          * a[-1], a[0] * a[1], a[-1] * a[-2]))


solve()
