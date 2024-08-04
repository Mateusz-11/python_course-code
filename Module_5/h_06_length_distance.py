from math import sqrt

def calculate_segment_lenght(start: tuple, end:tuple) -> float:
    x1, y1 = start
    x2, y2 = end

    return sqrt((x2-x1)**2+(y2-y1)**2)


print(calculate_segment_lenght((0,0), (0, 4)))