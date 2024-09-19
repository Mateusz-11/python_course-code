from dataclasses import field
from math import pi


class Circle:
    def __init__(self, radius_of_circle: int):
        self.radius_of_circle = radius_of_circle

    def get_circumference_of_wheel(self) -> float:
        return 2 * pi * self.radius_of_circle

    def get_circle_area(self) -> float:
        return pi * self.radius_of_circle ** 2

def test_circle_calculation():
    first_circle = Circle(5)
    area = first_circle.get_circle_area()
    circumference = first_circle.get_circumference_of_wheel()

    assert 78.5 < area < 78.6
    assert 31.4 < circumference < 31.5

test_circle_calculation()

## part 2
if __name__ == '__main__':
    radius = int(input('Podaj promie: '))
    circle = Circle(radius)
    print('Pole kołą wynosi: ', circle.get_circle_area())
    print('Obwód koła wynosi: ', circle.get_circumference_of_wheel())