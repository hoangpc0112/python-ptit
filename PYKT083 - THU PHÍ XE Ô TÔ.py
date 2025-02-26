def solve():
    dict = {}
    n = int(input())

    for _ in range(n):
        bien, xe, so, huong, ngay = input().split()

        if huong == 'OUT':
            continue

        if ngay not in dict:
            dict[ngay] = 0

        if so == '2':
            dict[ngay] += 20_000
        elif so == '5':
            dict[ngay] += 10_000
        elif so == '7':
            dict[ngay] += 15_000
        elif so == '29':
            dict[ngay] += 50_000
        else:
            dict[ngay] += 70_000

    for key in dict.keys():
        print(f"{key}: {dict[key]}")


solve()
