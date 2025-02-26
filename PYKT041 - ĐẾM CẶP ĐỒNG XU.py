from math import comb


def solve():
    n = int(input())
    a = [input().strip() for _ in range(n)]

    res = 0

    for i in range(n):
        cnt_row = 0
        cnt_col = 0

        for j in range(n):
            if a[i][j] == 'C':
                cnt_row += 1
            if a[j][i] == 'C':
                cnt_col += 1

        res += comb(cnt_row, 2) if cnt_row >= 2 else 0
        res += comb(cnt_col, 2) if cnt_col >= 2 else 0

    print(res)


solve()
