from dataclasses import dataclass


@dataclass
class Invoice:
    id: str
    name: str
    total: float

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.total:.0f}'


def solve():
    n = int(input())
    invoices = []

    for i in range(n):
        id = f"KH{i + 1:02}"
        name = input()
        num = -float(input()) + float(input())
        total = 0

        if num <= 50:
            # 50 số đầu giá 100
            total = num * 100 * 1.02
        elif num <= 100:
            # 50 số đầu giá 100, số còn lại giá 150
            total = (50 * 100 + (num - 50) * 150) * 1.03
        else:
            # 50 số đầu giá 100, 50 số tiếp theo giá 150, số còn lại giá 200
            total = (50 * 100 + 50 * 150 + (num - 100) * 200) * 1.05

        invoices.append(Invoice(id, name, total))

    invoices.sort(key=lambda x: (-x.total, x.id))

    for invoice in invoices:
        print(invoice)


solve()
