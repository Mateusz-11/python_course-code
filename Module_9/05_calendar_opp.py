from datetime import datetime


class Meeting:
    def __init__(self, date_of_meeting: datetime, title: str):
        self.title = title
        self.date_of_meeting = date_of_meeting

class Calendar:
    def __init__(self):
        self.meetings = {}

    def check_available(self, date_of_meeting: datetime):
        return date_of_meeting not in self.meetings

    def add_meeting(self, meeting: Meeting):
        self.meetings[meeting.date_of_meeting] = meeting

    def show_meetings(self, day: datetime=None):
        if day is None:
            return self.meetings

        meetings = []
        for meeting in self.meetings.values():
            if meeting.date_of_meeting.date() == day.date():
                meetings.append(meeting)

        return meetings


def test_meeting_creation():
    meeting = Meeting(datetime(2023, 11, 9, 19, 00), 'Meeting 001')
    assert meeting.title == 'Meeting 001'
    assert meeting.date_of_meeting == datetime(2023,11,9,19,00)

def test_meeting_in_calendar():
    meeting = Meeting(datetime(2023,11,9,19,00), 'Meeting 001')
    calendar = Calendar()
    calendar.add_meeting(meeting)

    assert len(calendar.meetings) == 1
    assert calendar.meetings[datetime(2023,11,9,19,00)].title == 'Meeting 001'

def test_get_meetings():
    meeting1 = Meeting(datetime(2023, 11, 9, 19, 00), 'Meeting 001')
    meeting2 = Meeting(datetime(2023, 10, 3, 19, 00), 'Meeting 002')
    calendar = Calendar()
    calendar.add_meeting(meeting1)
    calendar.add_meeting(meeting2)

    meetings = calendar.show_meetings()
    assert len(meetings) == 2

    meetings = calendar.show_meetings(datetime(2023,10,3))
    assert meetings[0].title == 'Meeting 002'

