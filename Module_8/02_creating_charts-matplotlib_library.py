import matplotlib.pyplot as plt

fig, ax = plt.subplots()

cities = ['Gdynia', 'Gdańsk', 'Sopot']
people = [220, 250, 300]

ax.bar(cities,people)
plt.show()