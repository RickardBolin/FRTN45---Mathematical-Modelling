import numpy
import clusters
import matplotlib.pyplot as plt

for size in range(11):
    size = size + 10
    list_of_clusters = []
    for foreach in range(10):
        BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
        loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
        list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
    cluster_mean = numpy.mean(list_of_clusters)
    print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 25
list_of_clusters = []
for foreach in range(10):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 30
list_of_clusters = []
for foreach in range(10):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 35
list_of_clusters = []
for foreach in range(10):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 40
list_of_clusters = []
for foreach in range(10):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))


size = 45
list_of_clusters = []
for foreach in range(5):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 50
list_of_clusters = []
for foreach in range(5):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 100
list_of_clusters = []
for foreach in range(5):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 150
list_of_clusters = []
for foreach in range(3):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 200
list_of_clusters = []
for foreach in range(2):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = sum(list_of_clusters) / float(len(list_of_clusters))
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

size = 250
list_of_clusters = []
for foreach in range(1):
    BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData/Vertex2D"
    loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# Glöm inte ändra "steps / 5" när om vi byter antal steps!
    list_of_clusters.append(clusters.clusters(loaded_world > 10000/5))
cluster_mean = numpy.mean(list_of_clusters)
print("Size: " + str(size) + "     " + "Clusters: " + str(cluster_mean))

fig = plt.figure()
plt.imshow(loaded_world)
plt.show()










# size = 18;
# distribution_of_clusters = []
# for foreach in range(10):
#     BASE_PATH = "/Users/Rickard/PycharmProjects/MatMod/MatmodData"
#     loaded_world = numpy.load(BASE_PATH + "/size" + str(size) + '_10000steps/' + str(foreach) + '.npy')
# # Glöm inte ändra "steps / 5" när om vi byter antal steps!
#     distribution_of_clusters.append(clusters.clusters(loaded_world > 10000/5))#
# #   cluster_mean = sum(list_of_clusters) / float(len(list_of_clusters))
# #    print("Size: " + str(size) + "     " + "Distribution of Clusters: " + str(cluster_mean))
# fig = plt.figure()
# plt.hist(distribution_of_clusters)
# plt.show()
