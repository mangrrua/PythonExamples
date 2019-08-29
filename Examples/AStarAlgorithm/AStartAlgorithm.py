import PriorityQueue
from collections import defaultdict

class Node:
    """
    Node class keeps node and its heuristic value
    """
    def __init__(self, node, heuristic):
        self._node = node
        self._heuristic = heuristic

    def get(self):
        return self._node

    def get_heuristic(self):
        return self._heuristic


class Graph:
    """
    Graph class keeps nodes and its adjacent, and applies A* star algorithm on these nodes
    """
    def __init__(self):
        self._nodes = {} 
        self._path = [] 

        self._destination_nodes = defaultdict(list)
        self._queue = PriorityQueue.PriorityQueue() 

    def add_adjacent(self, source_node, destination_node, cost):
        self._nodes[source_node] =  source_node
        self._nodes[destination_node] = destination_node
        self._destination_nodes[source_node.get()].append((destination_node, cost))

    def apply_a_star_algorithm(self, start_node, goal_node):
        """
        Define distances and parent_nodes list to find path.(Also known close list)

        Flow:
        - First of all, set all distances and parent_nodes to None. Then value will be assigned to these values
        - Calculate start node f_cost and insert this node with g_cost, h_cost and f_cost to open list
        - Until the queue is empty:
            - Get node that has minimum f_cost from open list
            - Find destination nodes f_cost, and insert to open list
            - If destination node's cost is not in distances list, insert it with cost.
              If previous cost is greater then destination nodes's cost, assign new cost for destination cost
              Also, add parent if destination node is not in list, and cost is greater then previous cost
              In short, if new_g_cost is lower than the previous g_cost for destination node,
              assign new parent for destination node for path.
            - Finally, is open list(queue) is empty, get goal node parent from parent list,
              and find path with back back tracking

        :param start_node: Starting node
        :param goal_node: Goal node
        :return: Shortest path
        """
        
        if start_node == goal_node: 
            return 0

        distances = {}
        parent_nodes = {}
        for node in self._nodes:
            distances[node.get()] = None
            parent_nodes[node.get()] = None

        distances[start_node.get()] = 0

        g_cost, h_cost = 0, start_node.get_heuristic()
        f_cost = g_cost + h_cost
        self._queue.insert((start_node, g_cost, h_cost), f_cost)

        while True:
            current_node, g_cost, h_cost = self._queue.get_and_remove()                 
            
            for dest_node, cost in self._destination_nodes[current_node.get()]:
                total_g_cost = g_cost + cost
                h_cost = dest_node.get_heuristic()
                f_cost = total_g_cost + h_cost
                self._queue.insert((dest_node, total_g_cost, h_cost), f_cost)

                if distances[dest_node.get()]:
                    if distances[dest_node.get()] > total_g_cost:
                        distances[dest_node.get()] = total_g_cost
                        parent_nodes[dest_node.get()] = current_node.get()
                else:
                    distances[dest_node.get()] = total_g_cost
                    parent_nodes[dest_node.get()] = current_node.get()

            if self._queue.is_empty(): 
                curr_node = goal_node.get()
                while curr_node:
                    self._path.append(curr_node)
                    curr_node = parent_nodes[curr_node]
                # Reverse list for print path
                self._path = self._path[::-1]
                return self._path


# Nodes with heuristic values
S = Node('S', 4)
A = Node('A', 2)
B = Node('B', 6)
C = Node('C', 2)
D = Node('D', 3)
G = Node('G', 0)

# Graph, and add nodes with adjacent and related costs.
graph = Graph()

graph.add_adjacent(S, G, 12)
graph.add_adjacent(S, A, 1)
graph.add_adjacent(A, B, 3)
graph.add_adjacent(A, C, 1)
graph.add_adjacent(B, D, 3)
graph.add_adjacent(C, D, 1)
graph.add_adjacent(C, G, 3)
graph.add_adjacent(D, G, 3)

path = graph.apply_a_star_algorithm(S, G)
[print("-->", node) for node in path]
