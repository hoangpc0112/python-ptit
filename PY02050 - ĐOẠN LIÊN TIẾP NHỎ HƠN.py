def solve():
    n = int(input())
    a = list(map(int, input().split()))

    st = []
    res = []

    for i in range(n):
        while len(st) > 0 and a[i] >= a[st[-1]]:
            st.pop()

        if len(st) == 0:
            res.append(i + 1)
        else:
            res.append(i - st[-1])

        st.append(i)

    print(*res)


for i in range(int(input())):
    solve()
