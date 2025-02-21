from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Point:
    x: Decimal
    y: Decimal

    def distance(self, p):
        return round(((self.x - p.x) ** 2 + (self.y - p.y) ** 2).sqrt(), 4)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
