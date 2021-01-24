# VERTEX2D

import numpy
import random
import matplotlib.pyplot as plt
import time as time
import os
import clusters

t0 = time.time()


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
            return (loc[0] - 1) % self.size, loc[1]  # left
        if tot * r < left + right:
            return (loc[0] + 1) % self.size, loc[1]  # right
        if tot * r < left + right + down:
            return loc[0], (loc[1] - 1) % self.size  # down
        return loc[0], (loc[1] + 1) % self.size  # up

    def update_vertices(self):
        for move in self.moves:
            self.vertices[move.new_loc] += move.n
        self.moves = []


size = 25

for iterations in range(10):
    world = World2D(size)
    ants = []
    for row in range(size):
        for col in range(size):
            ants.append(Ant2D(world, (row, col)))

    # fig = plt.figure()
    steps = 10000

    for k in range(steps):
        for ant in ants:
            ant.next_step()
        world.update_vertices()

    first_half = world.vertices.copy()

    for k in range(steps):
        for ant in ants:
            ant.next_step()
        world.update_vertices()

    second_half = world.vertices - first_half + 1

    temp = numpy.log(first_half)
    # plt.subplot(1, 2, 1)
    # plt.imshow(temp)
    #for r in range(size):
        #for c in range(size):
            #plt.text(c, r, first_half[r, c], horizontalalignment='center', fontsize='6')

    temp = numpy.log(second_half)
    #plt.subplot(1, 2, 2)

    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D/size25_10000steps"

    numpy.save(os.path.join(BASE_PATH, str(iterations)), second_half)

    # plt.imshow(test)


    # plt.imshow(temp)
    #  for r in range(size):
    #      for c in range(size):
    #          plt.text(c, r, second_half[r, c], horizontalalignment='center', fontsize='6')

    t1 = time.time()
    total = t1 - t0
    print(total)
    # cluster_count = clusters.clusters(second_half > steps / 5)
    #  print("Clusters: ", cluster_count)
    #  plt.show()
