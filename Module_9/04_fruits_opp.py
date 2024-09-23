from random import choice


class Apple:
    def __init__(self, color: str,taste: str, apple_type: str):
        self.color = color
        self.taste = taste
        self.apple_type = apple_type

    def get_info(self):
        return f'To jest {self.color}, {self.taste}, {self.apple_type} jabłko.'

class Basket:
    def __init__(self):
        self.apples = []

    def add_apple(self, apple: Apple):
        self.apples.append(apple)


class Report:
    def get_report(self, property: str, basket: Basket):
        statistics = {}
        for apple in basket.apples:
            if property == 'color':
                statistics.update({apple.color: statistics.get(apple.color, 0) + 1})
            elif property == 'taste':
                statistics.update({apple.taste: statistics.get(apple.taste, 0) + 1})
            elif property == 'apple_type':
                statistics.update({apple.apple_type: statistics.get(apple.apple_type, 0) + 1})

        return statistics

colors = ('zielone', 'czerwone', 'żółte')
tastes = ('cierpkie', 'słodkie', 'kwaśne')
apple_type = ('dojrzałe', 'niedojrzałe')

basket = Basket()
for _ in range(100):
    apple = Apple(choice(colors), choice(tastes), choice(apple_type))
    print(apple.get_info())
    basket.add_apple(apple)

report = Report()
print(report.get_report('apple_type', basket))
print(report.get_report('color', basket))
print(report.get_report('taste', basket))