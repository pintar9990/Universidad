from collections import namedtuple
import networkx as nx
import math
import os

Point = namedtuple("Point", ['x', 'y'])


def length(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def complete_graph(points):
    """ Creates a complete graph """
    graph =nx.MultiGraph()

    print(points)

    for i in range (0, len(points)):
        graph.add_node(points[i])

    for x in range (0, len(points)): # debería ir item count
        for y in range (1, len(points)):
            if ((y > x) and (y != x)):
                graph.add_edge(x, y, weight=length(points[x],points[y]))


    return graph


def solve_2_approx(points):
    """ implements the Tree 2-approximate algorithm for TSP """
    graphfull = nx.complete_graph(points)

    for x in range (1, len(points)): # debería ir item count
        for y in range (1, len(points)):
            if ((y > x) and (y != x)):
                graphfull.add_edge(x, y, weight=(points[x],points[y]))

    lista = nx.minimum_spanning_tree(graphfull)

    return None
