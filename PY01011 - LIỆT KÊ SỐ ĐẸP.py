a = []


def backtrack(i):
    if int(i) > 888:
        return

    a.append(int(i + i[::-1]))

    backtrack(i + '0')
    backtrack(i + '2')
    backtrack(i + '4')
    backtrack(i + '6')
    backtrack(i + '8')


def solve():
    n = int(input())

    for i in a:
        if i < n:
            print(i, end=" ")
        else:
            break

    print()


backtrack("2")
backtrack("4")
backtrack("6")
backtrack("8")

a.sort()

t = int(input())
for i in range(t):
    solve()
