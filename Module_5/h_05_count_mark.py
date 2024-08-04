def get_note(mark: int, total_mark: int = 100) -> str:
    result = mark / total_mark
    match result:
        case result if result <= 0.4:
            return "weak"
        case result if 0.4 < result <= 0.6:
            return "satisfactory"
        case result if 0.6 < result <= 0.8:
            return "good"
        case result if 0.8 < result <= 1.0:
            return "excellent"
        case _:
            return "Wrong value"


print(get_note(50, 100))
print(get_note(30, ))
print(get_note(70, ))
