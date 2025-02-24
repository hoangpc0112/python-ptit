from dataclasses import dataclass


@dataclass
class Customer:
    id: str
    name: str
    playtime: int

    def __str__(self):
        return f"{self.id}  {self.name} {self.playtime // 60} gio {self.playtime % 60} phut"


def solve():
    n = int(input())
    customers = []

    for i in range(n):
        id = input()
        name = input()
        start = input().split(":")
        end = input().split(":")

        playtime = (int(end[0]) - int(start[0])) * \
            60 + int(end[1]) - int(start[1])

        customers.append(Customer(id, name, playtime))

    customers.sort(key=lambda x: -x.playtime)

    for customer in customers:
        print(customer)


solve()
