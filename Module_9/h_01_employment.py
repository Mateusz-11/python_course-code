from datetime import date, datetime


class InvalidDateOfEmployment(Exception):
    pass

class BaseEmployee:
    def __init__(self, first_name: str, last_name: str, employment_date: date):
        today = datetime.today().date()
        employment_time = today.year - employment_date.year

        if employment_date > today or employment_time > 50:
            raise InvalidDateOfEmployment('Wrong employment date!')

        self.employment_date = employment_date
        self.last_name = last_name
        self.first_name = first_name

    def __lt__(self, other):
        return self.employment_date < other.employment_date

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def get_employment_time(self):
        today = datetime.today().date()
        employment_time = today - self.employment_date

        return employment_time.days

class Employee(BaseEmployee):
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 employment_date: date,
                 hourly_rate: float,
                 number_of_hours: int,
                 bonus: int= 0):

        super().__init__(first_name, last_name, employment_date)
        self.bonus = bonus
        self.number_of_hours = number_of_hours
        self.hourly_rate = hourly_rate

    def get_salary(self):
        return self.hourly_rate * self.number_of_hours + self.bonus

empl1 = BaseEmployee('A', 'B', date(2000, 11,12))
empl2 = BaseEmployee('C', 'D', date(2000, 10,12))
empl3 = BaseEmployee('E', 'F', date(2000, 12,15))
# empl4 = BaseEmployee('C', 'D', date(2025, 11,12))
# empl5 = BaseEmployee('E', 'F', date(1950, 11,12))

employees = [empl3, empl2, empl1]
employees.sort()
print(employees)