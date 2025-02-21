from dataclasses import dataclass


@dataclass
class Student:
    name: str
    aced: int
    submitted: int


def solve():
    n = int(input())
    students = []

    for _ in range(n):
        name = input()
        aced, submitted = map(int, input().split())
        students += [Student(name, aced, submitted)]

    students.sort(key=lambda x: (-x.aced, x.submitted, x.name))

    for i in students:
        print(f"{i.name} {i.aced} {i.submitted}")


solve()
