import numpy as np

class Lattice:
    def __init__(self, num_nodes=26):
        self.num_nodes = num_nodes
        self.nodes = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:num_nodes]
        self.frequencies = np.linspace(0.040, 0.780, num_nodes)

    def display(self):
        print("Node | Frequency (Hz)")
        for node, freq in zip(self.nodes, self.frequencies):
            print(f"{node}    | {freq:.4f}")

    def get_frequencies(self):
        return self.frequencies
