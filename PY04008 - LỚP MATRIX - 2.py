from dataclasses import dataclass


@dataclass
class Matrix:
    rows: int
    cols: int
    data: list

    def transpose(self) -> 'Matrix':
        b = []

        for i in range(self.cols):
            b.append([0] * self.rows)

        for i in range(self.rows):
            for j in range(self.cols):
                b[j][i] = self.data[i][j]

        return Matrix(self.cols, self.rows, b)

    def multiply(self, other: 'Matrix') -> 'Matrix':
        res = []

        for i in range(self.rows):
            res.append([0] * other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    res[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(self.rows, other.cols, res)


num = []
start = 0


def solve():
    global start

    n = num[start]
    m = num[start + 1]
    a = []

    start += 2

    for i in range(n):
        a.append([0] * m)

    for i in range(n):
        for j in range(m):
            a[i][j] = num[start + j]

        start += m

    x = Matrix(n, m, a)
    y = x.transpose()
    res = x.multiply(y)

    for i in range(res.rows):
        for j in range(res.cols):
            print(res.data[i][j], end=' ')

        print()


t = int(input())

while True:
    try:
        num.extend(map(int, input().split()))
    except Exception:
        break

for i in range(t):
    solve()
