class LengthUnit:
    def __init__(self, value:int):
        self.value = value

    def __str__(self):
        return f'{self.value} mm'

    def __add__(self, other):
        return LengthUnit(self.value + other.value)

    def __sub__(self, other):
        return LengthUnit(self.value - other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return  self.value > other.value

    def __ge__(self, other):
        return  self.value > other.value

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100


v1 = LengthUnit(300)
print(v1)
v2 = LengthUnit(750)
print(v2)

v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)

print(v1 != v3)
print(v1 > v3)
print(v1 >= v3)
