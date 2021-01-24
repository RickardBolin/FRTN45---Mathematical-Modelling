# EDGE 1D

import numpy
import matplotlib.pyplot as plt
import random
import time

t0 = time.time()


class Ant1D:
    def __init__(self, world, loc):
        self.world = world
        self.loc = loc

    def next_step(self):
        new_loc = self.world.random_neighbor(self.loc)
        edge = min(self.loc, new_loc)
        world.change_in_edges.append((edge, 1))
        self.loc = new_loc


class World1D:
    change_in_edges = []

    def __init__(self, size):
        self.edges = numpy.ones(size, int)
        self.size = size

    def random_neighbor(self, loc):
        left = self.edges[loc - 1]
        right = self.edges[loc]
        r = random.uniform(0, 1)
        if r < left / (left + right):
            return (loc - 1) % self.size
        return (loc + 1) % self.size

    def update_edges(self):
        for c in self.change_in_edges:
            self.edges[c[0]] += c[1]
        self.change_in_edges = []


fig = plt.figure()
world = World1D(30)
ants = []
for i in range(1):
    ants.append(Ant1D(world, 15))


for k in range(10000):
    for ant in ants:
        ant.next_step()
    world.update_edges()

plt.yscale('log')
plt.stem(range(30), world.edges)

t1 = time.time()
total = t1 - t0
print(total)
plt.show()
