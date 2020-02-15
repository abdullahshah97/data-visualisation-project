import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolor='none', s=2)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis='both', which ='major', labelsize=14)

plt.show()
# can alternatively save instead of just showing by running
# plt.savefig('file_name.png')
