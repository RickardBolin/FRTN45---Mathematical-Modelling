#VERTEX2D, simulation

import numpy
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt


class Ant2D:
    def __init__(self, world, loc):
        self.world = world
        self.loc = loc

    def next_step(self):
        new_loc = self.world.random_neighbor(self.loc)
        world.moves.append(Move(self.loc, new_loc, 1))
        self.loc = new_loc


class Move:
    def __init__(self, old_loc, new_loc, n):
        self.new_loc = new_loc
        self.n = n


class World2D:
    moves = []

    def __init__(self, size):
        self.size = size
        self.vertices = numpy.ones((size, size), int)

    def random_neighbor(self, loc):
        left = self.vertices[loc[0] - 1, loc[1]]
        right = self.vertices[(loc[0] + 1) % self.size, loc[1]]
        down = self.vertices[loc[0], loc[1] - 1]
        up = self.vertices[loc[0], (loc[1] + 1) % self.size]
        r = random.uniform(0, 1)
        tot = left + right + down + up
        if tot * r < left:
            return (loc[0] - 1) % self.size, loc[1] # left
        if tot * r < left + right:
            return (loc[0] + 1) % self.size, loc[1]  # right
        if tot * r < left + right + down:
            return loc[0], (loc[1] - 1) % self.size  # down
        return loc[0], (loc[1] + 1) % self.size  # up

    def update_vertices(self):
        for move in self.moves:
            self.vertices[move.new_loc] += move.n
        self.moves = []


world_size = 15
world = World2D(world_size)
ants = []
for index in range(10):
    ants.append(Ant2D(world, (random.randint(0, world_size - 1), random.randint(0, world_size - 1))))
fig = plt.figure()


def animate(k):
    for ant in ants:
        ant.next_step()
    world.update_vertices()
    if k % 99 == 0:
        temp = numpy.log(world.vertices)
        plt.cla()
        plt.imshow(temp)
        for r in range(len(world.vertices)):
            for c in range(len(world.vertices)):
                plt.text(c, r, world.vertices[r, c], horizontalalignment='center', fontsize='8')
                for ant in ants:
                    if (r, c) == ant.loc:
                        plt.plot(c, r, '*')


ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
