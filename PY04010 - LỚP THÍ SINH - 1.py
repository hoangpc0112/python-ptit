from dataclasses import dataclass


@dataclass
class Student:
    full_name: str
    date_of_birth: str
    total_points: float

    def __str__(self) -> str:
        return f"{self.full_name} {self.date_of_birth} {self.total_points:.1f}"


def solve():
    print(Student(input(), input(), float(
        input()) + float(input()) + float(input())))


solve()
