import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make a random walk and plot the points
#Keep making random walks whiile program is active
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=2)
    plt.show()

    cont = input("Make another walk? (y/n): ")
    if cont == 'n':
        break
