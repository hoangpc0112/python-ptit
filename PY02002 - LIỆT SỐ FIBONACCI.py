fibo = [0, 1]


def fibonacci():
    for i in range(2, 93):
        fibo.append(fibo[i - 1] + fibo[i - 2])


def solve():
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        print(fibo[i], end=" ")

    print()


fibonacci()
for i in range(int(input())):
    solve()
