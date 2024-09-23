from datetime import datetime


class Meeting:
    def __init__(self, date_of_meeting: datetime, title: str):
        self.title = title
        self.date_of_meeting = date_of_meeting

class Calendar:
    def __init__(self):
        self.meetings = {}

    def show_meetings(self):
        return 1

    def check_the_date(self):
        return 1




