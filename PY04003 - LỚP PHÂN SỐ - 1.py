from dataclasses import dataclass
from math import gcd


@dataclass
class Fraction:
    numerator: int
    denominator: int

    def __str__(self):
        f_gcd = gcd(self.numerator, self.denominator)
        return "{}/{}".format(self.numerator // f_gcd, self.denominator // f_gcd)


def solve():
    a, b = map(int, input().split())
    print(Fraction(a, b))


solve()
