def solve():
    n = int(input())
    a = list(map(float, input().split()))

    a.sort()

    sum = 0
    cnt = 0

    for i in a:
        if i != a[0] and i != a[-1]:
            sum += i
            cnt += 1

    print(round(sum / cnt, 2))


solve()
