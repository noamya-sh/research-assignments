import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways

n, l, e = [int(i) for i in input().split()]
links = []
ga = set()

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links.append((n1,n2))
for i in range(e):
    ga.add(int(input()))  # the index of a gateway node
gw_edges = [tup for tup in links if tup[0] in ga  or tup[1] in ga]

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    # get edge between agent and gateway
    neighbor = [tup for tup in gw_edges if tup[0] == si or tup[1] == si]
    if len(neighbor) > 0:
        n1, n2 = neighbor.pop()
    else:
        n1, n2 = gw_edges.pop()
    print(n1,n2)
