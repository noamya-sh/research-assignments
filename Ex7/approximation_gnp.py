import networkx as nx
from networkx.algorithms.approximation import clique
import math
import matplotlib.pyplot as plt


def gnp(n: int, p: float):
    return nx.gnp_random_graph(n, p)


def max_clique_approximation(g):
    return len(clique.max_clique(g))


def max_clique_real(g):
    return len(max(nx.find_cliques(g), key=lambda x: len(x)))


def plot_apx_vs_real(prob: list, idx: list, size_v: int):
    fig, axs = plt.subplots(2, 2, figsize=(12, 9))

    for p, ind in zip(prob, idx):
        k = []
        j = []
        r = []
        for i in range(1, size_v + 1):
            g = gnp(i, p)
            if i != 1:
                ratio = i / (math.log(i) ** 2)
            else:
                ratio = 0
            r.append(ratio)
            k.append(max_clique_approximation(g))
            j.append(max_clique_real(g))
        axs[ind].plot(k, 'gold', j, 'navy', r, '--')
        axs[ind].set_title("probability = {x}".format(x=p))
    fig.figure.supxlabel("number of vertices of graph")
    fig.figure.supylabel("size max clique of graph")
    fig.figure.legend(["real_approx", "real max clique", "approx ratio"])
    plt.show()


plot_apx_vs_real([0.9, 0.7, 0.5, 0.25], [(0, 0), (0, 1), (1, 0), (1, 1)], 100)
