from datetime import datetime


class Meeting:
    def __init__(self, title: str, date_of_meeting: datetime, room: str):
        self.title = title
        self.date_of_meeting = date_of_meeting
        self.room = room

