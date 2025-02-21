from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int
    height: int
    colored: str

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def color(self):
        return self.colored.capitalize()


arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print("{} {} {}".format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
