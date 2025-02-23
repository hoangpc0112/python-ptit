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


def solve():
    n, m = map(int, input().split())

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    x = Matrix(n, m, a)
    y = x.transpose()
    res = x.multiply(y)

    for i in range(res.rows):
        for j in range(res.cols):
            print(res.data[i][j], end=' ')

        print()


for i in range(int(input())):
    solve()
