def solve():
    s = input()
    f = [0] * 10

    def backtrack(res):
        if len(res) == len(s):
            print(res)
            return

        for i in range(len(s)):
            if f[i] == 0:
                f[i] = 1
                backtrack(res + s[i])
                f[i] = 0

    backtrack('')


solve()
