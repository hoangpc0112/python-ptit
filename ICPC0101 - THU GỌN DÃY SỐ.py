def solve():
    n = int(input())
    a = list(map(int, input().split()))
    st = []

    for i in a:
        if len(st) == 0:
            st.append(i)
        else:
            if not (st[-1] + i) & 1:
                st.pop()
            else:
                st.append(i)

    print(len(st))


solve()
