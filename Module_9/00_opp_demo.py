class Student:
    def __init__(self, first_name: str, last_name: str, semester: int = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester
        self.notes = []

    def promote(self):
        self.semester =+ 1

    def add_note(self, note: int):
        if note > 6 or note < 1:
            return

        self.notes.append(note)

    def get_average(self):
        return sum(self.notes) / len(self.notes)

john = Student('John', 'Smith')
john.add_note(5)
john.add_note(4)
john.add_note(6)
print(john.notes)
print(john.get_average())
print(john.semester)