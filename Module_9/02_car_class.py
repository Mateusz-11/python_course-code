class Car:
    def __init__(self, name: str, price: int, max_speed: int):
        self.name = name
        self.price = price
        self.max_speed = max_speed

cars = []
for _ in range(5):
    cars.append(Car(
        input('Podaj nazwę: '),
        int(input('Podaj cenę: ')),
        int(input('Podaj prędkość maksymalną: ')),
    ))
    print('- - - ' * 3)

for car in cars:
    print(car.name, car.price, car.max_speed)