"""
This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.
"""


class GraphPath:
    def __init__(self, nodes=set(), letter_counts=dict()):
        self.nodes = nodes
        self.letter_counts = letter_counts

    def __repr__(self):
        return "nodes={}, letters={}".format(self.nodes, self.letter_counts)

def get_max_value_string(graph_path, node, adjacency_map):
    if node in graph_path.nodes:
        return [graph_path]

    new_nodes = graph_path.nodes.copy()
    new_nodes.add(node)
    new_letter_counts = graph_path.letter_counts.copy()
    if node[0] not in new_letter_counts:
        new_letter_counts[node[0]] = 0
    new_letter_counts[node[0]] += 1

    new_graph_path = GraphPath(new_nodes, new_letter_counts)

    if node not in adjacency_map:
        return [new_graph_path]

    paths = list()
    for child_node in adjacency_map[node]:
        new_paths = get_max_value_string(
            new_graph_path, child_node, adjacency_map)
        paths.extend(new_paths)
    return paths

def get_max_value_string_helper(graph_string, edge_list):

    letter_counts = dict()
    nodes = list()
    for char in graph_string:
        if char not in letter_counts:
            letter_counts[char] = 0
        else:
            letter_counts[char] += 1
        nodes.append("{}{}".format(char, letter_counts[char]))
    # print(letter_counts)
    print(nodes)

    adjacency_map = dict()
    for start, end in edge_list:
        if nodes[start] not in adjacency_map:
            adjacency_map[nodes[start]] = set()
        if nodes[start] != nodes[end]:
            adjacency_map[nodes[start]].add(nodes[end])
    print(adjacency_map)

    paths = list()
    graph_path = GraphPath()
    for node in adjacency_map:
        new_paths = get_max_value_string(graph_path, node, adjacency_map)
        paths.extend(new_paths)

    max_value = 0
    for path in paths:
        max_path_value = max(path.letter_counts.values())
        if max_path_value > max_value:
            max_value = max_path_value

    print(max_value)
    return max_value if max_value > 0 else None



assert get_max_value_string_helper("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]) == 3
assert not get_max_value_string_helper("A", [(0, 0)])
