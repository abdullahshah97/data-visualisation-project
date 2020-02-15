import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make a random walk and plot the points
#Keep making random walks whiile program is active
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s = 50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s =50)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    cont = input("Make another walk? (y/n): ")
    if cont == 'n':
        break
