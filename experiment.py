from aloha import Aloha
import matplotlib.pyplot as pl

# number of nodes
n = 20

# vector of message generation probabilities
q = [0.2, 0.4, 0.6, 0.8]

# number of epochs
e = 20000

# vector of probabilities of sending
p = [i / 100 for i in range(10, 100, 10)]

# list of lists that contain accuracy for each p
accuracies = [[], [], [], []]

# list of lists that contain average node latencies for each p
avg_node_latencies = [[], [], [], []]

# colors for line plotting
colors = ['b', 'g', 'r', 'c']

A = pl.figure(1)

# experiment will be conducted for various q values
# that will be represented with different line colors
for j in range(4):
    for i in p:
        x = Aloha(n, i, q[j], e)
        x.simulate()
        accuracies[j].append(x.result.count(True) / e)
        # print(x.node_latencies)
        avg_node_latencies[j].append(x.comp_avg_node_latency())
        # print(avg_node_latencies[j])
    pl.plot(p, accuracies[j], colors[j])


pl.xlabel('Probability of sending')
pl.ylabel('Network accuracy')
A.show()

L = pl.figure(2)

for j in range(4):
    pl.plot(p, avg_node_latencies[j], colors[j])

pl.xlabel('Probability of sending')
pl.ylabel('Average node latency')
pl.show()
