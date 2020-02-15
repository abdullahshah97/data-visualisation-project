import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter( x_values, y_values, s=1)

plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Values", fontsize=14)
plt.title("Cube of numbers", fontsize = 20)

plt.axis([0, 5000, 0 ,125000000000])

plt.show()
