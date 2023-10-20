import matplotlib.pyplot as plt

fig, ax = plt.subplots()

agazatok = ['Erősáramú\nelektrotechnikus', 'Ipari \ninformatikai\n technikus', 'Szoftverfejlesztő \nés -tesztelő', 'Informatikai \nrendszer- és\n alkalmazás-üzemeltető']
counts = [40, 100, 30, 55]
bar_labels = ['Erősáramú elektrotechnikus', 'Ipari informatikai technikus', 'Szoftverfejlesztő és -tesztelő', 'Informatikai rendszer- és alkalmazás-üzemeltető']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(agazatok, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Fő')
ax.set_title('Nyílt napon választott szakok aránya ')
ax.legend(title='Választott szakok')

plt.show()