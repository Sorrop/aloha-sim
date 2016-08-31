import random


class Aloha():
    '''
    Aloha network simulation.Each node tries to send into a single channel.
    It generates a message (becomes active) with probability q.
    Then it tries to send the message into the channel with probability p.
    If more than one nodes try to send, collision occurs resulting to failure,
    otherwise transmission is succesful.
    '''

    def __init__(self, nodes, p_send, q_generate, epochs):
        # number of nodes
        self.nodes = nodes

        # probability that an active node will send the generated message
        self.p_send = p_send

        # probability that a node will generate a message
        self.q_generate = q_generate

        # number of time steps to simulate
        self.epochs = epochs

        # list with the state of each node, initially all inactive
        self.states = [False] * self.nodes

        # list of current latencies for each node
        self.latencies = [0] * self.nodes

        # dictionary of nodes that keeps track of the total latency
        # that a node experienced in each interval that was latent.
        # It will be used to measure the average latency
        # for each node and total average latency.
        self.node_latencies = {i: [] for i in range(self.nodes)}

        # list of transmission outcomes. True for succes
        self.result = []

    def message_generation(self):
        '''
        Helper function to check message generation
        '''
        for i in range(len(self.states)):
            # need only to check for inactive nodes
            if not self.states[i]:
                if random.random() <= self.q_generate:
                    self.states[i] = True

    def transmission(self):
        senders = []
        actives = []

        # gather the indices of all active nodes
        actives = [i for i in range(len(self.states)) if self.states[i]]

        # check if an active node will try to send
        senders = [actv for actv in actives if random.random() <= self.p_send]

        # If more than one try to send we have a collision that results
        # in transmission failure
        if len(senders) > 1:
            self.result.append(False)
            # so any active node experiences latency
            for active in actives:
                self.latencies[active] += 1

        else:
            # If none wants to send then certainly we don't experience failure
            if not senders:
                self.result.append(True)
                # but we might experience latency
                for active in actives:
                    self.latencies[active] += 1
            else:
                # Success. Only one node tries to send
                self.states[senders[0]] = False
                # keep track of the possible latency the node has experienced
                self.node_latencies[senders[0]].append(self.latencies[senders[0]])                # the sender is not latent now
                self.latencies[senders[0]] = 0
                # all other active nodes experience latency again
                actives.remove(senders[0])
                for active in actives:
                    self.latencies[active] += 1
                self.result.append(True)

    def simulate(self):
            for i in range(self.epochs):
                self.message_generation()
                self.transmission()

    def comp_avg_node_latency(self):
        '''
        Method to compute the average node latency
        '''
        avg = 0

        # it is possible for a node not to experience latency at all
        # we omit such cases from computation
        for node in range(self.nodes):
            y = [value for value in self.node_latencies[node] if value]

            if y:
                avg += sum(y) / len(y)

        return avg / self.nodes

if __name__ == '__main__':
    '''
    Code to test the accuracy of the network (#succesful_transfers/#epochs)
    and latency for various values of p
    '''

    print('Exhibition:')
    x = Aloha(10, 0.1, 0.8, 25)
    x.simulate()
    print('Result: ' + str(x.result))
    print('Node latencies: ' + str(x.node_latencies))
    print('Average node latency: ' + str(x.comp_avg_node_latency()))
