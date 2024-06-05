# set_3 = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33}
set_3 = set(range(3, 100, 3))
# set_5 = {5, 10, 15, 20, 25, 30, 35}
set_5 = set(range(5, 100, 5))

common_set = set_3 & set_5

print(common_set)
