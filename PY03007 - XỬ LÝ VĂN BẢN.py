def solve():
    s = []

    while True:
        try:
            s += input().lower().split()
        except Exception:
            break

    is_first = True

    for i in range(len(s)):
        if is_first:
            s[i] = s[i].capitalize()
            is_first = False

        if s[i][-1] in '.!?':
            is_first = True
            print(s[i][:-1])
        else:
            print(s[i], end=' ')


solve()
