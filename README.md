# aloha-sim

Pure ALOHA scheme simulation in Python

This is a simplified <a href="https://en.wikipedia.org/wiki/ALOHAnet#ALOHA_protocol">pure ALOHA</a> simulation implementation written in Python.

We have a number of n nodes that use a single communication channel. In the middle of a time interval (epoch) a node produces a message with probability q and becomes active. When a node is active it will attempt to send the message with probability n.
When two nodes or more attempt to send, a collision occurs resulting in transmision failure. Otherwise (0 or 1 nodes attempt to send) we have a success.

<b>aloha.py</b> : The Aloha class is defined and initialized with parameters n, p, q, e(pochs). The core simulate() method makes use of methods message_generation() and transmission().

<b>experiment.py</b> : The behaviour of such a network is examined by running tests for various values of p,q for given number of nodes and a large number of epochs. Results are plotted into 2 graphs. Figure 1 shows the network's accuracy based on the choice of probabilithy of sending (p) and figure 2 the average latency per node for p. Different colors indicate different choice of q. 

