from dataclasses import dataclass


@dataclass
class Candidate:
    id: str
    name: str
    total_points: float
    classification: str

    def __str__(self):
        return f"{self.id} {self.name} {self.total_points:.2f} {self.classification}"


def solve():
    n = int(input())
    candidates = []

    for i in range(n):
        id = "TS0" + str(i + 1)  # Đề ảo
        name = input()
        point_1 = float(input())
        point_2 = float(input())
        total_points = 0
        classification = ""

        if point_1 > 10:
            point_1 /= 10
        if point_2 > 10:
            point_2 /= 10

        total_points = (point_1 + point_2) / 2

        if total_points < 5:
            classification = "TRUOT"
        elif total_points < 8:
            classification = "CAN NHAC"
        elif total_points <= 9.5:
            classification = "DAT"
        else:
            classification = "XUAT SAC"

        candidates.append(Candidate(id, name, total_points, classification))

    candidates.sort(key=lambda x: -x.total_points)

    for candidate in candidates:
        print(candidate)


solve()
