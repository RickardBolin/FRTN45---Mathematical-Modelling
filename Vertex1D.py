# VERTEX1D

import numpy
import random
import matplotlib.pyplot as plt
import time
import Clusters1D
import os

t0 = time.time()


class Ant1D:
    def __init__(self, world, loc):
        self.world = world
        self.loc = loc

    def next_step(self):
        self.loc = self.world.random_neighbor(self.loc)
        world.change_in_vertices.append((self.loc, 1))


class World1D:
    change_in_vertices = []

    def __init__(self, size):
        self.vertices = numpy.ones(size, int)
        self.size = size

    def random_neighbor(self, loc):
        left = self.vertices[(loc - 1)%self.size]
        right = self.vertices[(loc + 1)%self.size]
        r = random.uniform(0, 1)
        if r < left / (left + right):
            return (loc - 1) % self.size
        return (loc + 1) % self.size

    def update_vertices(self):
        for c in self.change_in_vertices:
            self.vertices[c[0]] += c[1]
        self.change_in_vertices = []


for size in range(45):
    size = size + 5
    for iterations in range(10):
        steps = 10000
        world = World1D(size)
        ants = []
        for loc in range(size):
            ants.append(Ant1D(world, loc))

        for k in range(steps):
            for ant in ants:
                ant.next_step()
            world.update_vertices()

        first_half = world.vertices.copy()

        for k in range(steps):
            for ant in ants:
                ant.next_step()
            world.update_vertices()

        second_half = world.vertices-first_half

        #plt.yscale('log')
        #plt.stem(range(l), second_half)

        t1 = time.time()
        total = t1 - t0
        print("Execution time: ", total)
        #plt.show()

        BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex1D"
        numpy.save(os.path.join(BASE_PATH + "/size" + str(size) + '_10000steps/', str(iterations)), second_half)
    print("Done with size" + str(size))

#cluster_count=Clusters1D.clusters(second_half>steps/5)
#print("Clusters: ",cluster_count)
