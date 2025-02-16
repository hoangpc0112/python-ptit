class Number:
    def __init__(self, n):
        self.n = n
        self.sum_digit = sum([int(i) for i in str(n)])


def solve():
    n = int(input())
    numbers = list(map(Number, list(map(int, input().split()))))
    numbers.sort(key=lambda x: (x.digitSum, x.n))
    print(" ".join([str(i.n) for i in numbers]))


for i in range(int(input())):
    solve()
