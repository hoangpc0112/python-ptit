def solve():
    s = input()
    cnt_up, cnt_low = 0, 0

    for i in s:
        if i.isupper():
            cnt_up += 1
        else:
            cnt_low += 1

    print(s.upper() if cnt_up > cnt_low else s.lower())


solve()
