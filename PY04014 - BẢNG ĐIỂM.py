from dataclasses import dataclass


@dataclass
class Student:
    id: str
    name: str
    avg_points: float
    type: str

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.avg_points:.1f} {self.type}"


def solve():
    n = int(input())
    Students = []

    for i in range(n):
        name = input()
        points = list(map(float, input().split()))
        avg_points = (sum(points) + points[0] + points[1]) / len(points) / 1.2
        type = "XUAT SAC" if avg_points >= 9 else "GIOI" if avg_points >= 8 else "KHA" if avg_points >= 7 else "TB" if avg_points >= 5 else "YEU"
        id = f"HS{i + 1:02}"

        Students.append(Student(id, name, avg_points, type))

    Students.sort(key=lambda x: (-x.avg_points, x.id))

    for student in Students:
        print(student)


solve()
