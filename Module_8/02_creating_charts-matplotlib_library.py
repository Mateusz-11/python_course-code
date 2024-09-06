import matplotlib.pyplot as plt

fig, ax = plt.subplots()

cities = ['Gdynia', 'Gdańsk', 'Sopot']
people = [220, 250, 300]

# Label / title
ax.set_xlabel('Miasta')
ax.set(ylabel='Ilość komentarzy', title='Ilość dodanych komentarzy')

ax.bar(cities,people)
# plt.show()

# save to file
# plt.savefig('nazwawykresu.jpg')

# !! Save or show !!