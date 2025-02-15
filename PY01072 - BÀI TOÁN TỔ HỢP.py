def solve():
    n, k = list(map(int, input().split()))
    a = sorted(set(map(int, input().split())))

    def backtrack(i, cnt, s):
        if cnt == k:
            print(s)
            return

        for j in range(i, len(a)):
            backtrack(j + 1, cnt + 1, s + str(a[j]) + ' ')

    backtrack(0, 0, '')


solve()
