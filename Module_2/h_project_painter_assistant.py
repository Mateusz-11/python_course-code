from math import ceil

numbers_of_wall = int(input('How many walls is to paint: '))
print('- - - ' * 10)
print('All values write in meters, e.g 3.2')
print('- - - ' * 10)
paint_performance = 13
base_performance = 5

total_area = 0

for counter in range(1, numbers_of_wall + 1):
    wall_height = round(float(input(f'Write the height of wall {counter}: ')), 2)
    wall_width = round(float(input(f'Write the width of wall {counter}: ')), 2)

    total_area += wall_width * wall_width
print('- - - ' * 10)
layers_of_base = int(input('How many layers of base you want to do: '))
layers_of_paint = int(input('How many layers of paint you want to do: '))
print('- - - ' * 10)

# Used 'ceil' to round up
litres_of_base = ceil(total_area * layers_of_base / base_performance)
litres_of_paint = ceil(total_area * layers_of_paint / paint_performance)

print(f'You will paint {total_area} metres of walls')
print(f'You need {litres_of_paint} litres of paint')
print(f'You need {litres_of_base} litres of base')
