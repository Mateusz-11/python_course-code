class Employee:
    def __init__(self, name: str, last_name: str, hourly_rate: int):
        self.hourly_rate = hourly_rate
        self.last_name = last_name
        self.name = name
        self.time = 0

    def add_time(self, time_in_h: int):
        self.time += time_in_h

    def get_salary(self) -> float:
        salary = self.time * self.hourly_rate
        self.time = 0

        return salary


class Manager(Employee):
    def __init__(self, name: str, last_name: str, hourly_rate: int):
        super().__init__(name, last_name, hourly_rate)
        self.bonus = 0

    def add_bonus(self, bonus: int):
        self.bonus += bonus

    def get_salary(self) -> float:
        return 2 * super().get_salary() + self.bonus


def test_employee():
    employee = Employee('Piotr', 'Nowak', 30)
    employee.add_time(100)

    assert employee.get_salary() == 30 * 100

def test_manager():
    manager = Manager('Bartłomiej', 'Kowalski', 40)
    manager.add_time(100)
    manager.add_bonus(500)

    assert manager.get_salary() == 40 * 100 * 2 + 500

