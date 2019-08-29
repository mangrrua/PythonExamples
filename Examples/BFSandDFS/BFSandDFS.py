import Queue, Stack

class Node:
	def __init__(self, name):
		self.name = name
		self.adjacents = []
		self.visited = False

	def add_addjacents(self, nodes):
		self.adjacents.extend(nodes)


class Graph:
	def __init__(self):
		self.nodes = []
		# Queue for BFS
		self._queue = Queue.Queue()
		# Stack for DFS
		self._stack = Stack.Stack()

	def add_nodes(self, nodes):
		self.nodes.extend(nodes)

	def BFS(self, start_node):
		"""
		BFS Algorithm; BFS searchs horizontally on the graph/tree. BFS algorithm uses queue as data structure.

		For example graph:
			A -> B, C, E, G
			B -> A
			C -> A
			D-> E, F
			F -> D, E, G
			G -> A, F

		For this graph, BFS can work like following;
			A, B, C, E, G, D, F

		Firstly, it look adjacent nodes of parent node, if all adjacent nodes of parent have been visited,
		then BFS begins to look at the adjacent nodes of adjacent node.

		:param start_node: Start node represents where the search start
		:return: Not return value
		"""

		start_node.visited = True
		self._queue.enqueue(start_node)
		print(start_node.name)

		while not self._queue.is_empty():
			current_node = self._queue.dequeue()
			for neighbour in current_node.adjacents:
				if neighbour.visited == False:
					neighbour.visited = True
					self._queue.enqueue(neighbour)
					print(neighbour.name)

	def DFS_RECURSIVE(self, node):
		"""
		DFS Algorithm; DFS searchs vertically on the graph/tree. This DFS works as recursive.

		For example graph:
			A -> B, C, E, G
			B -> A
			C -> A
			D-> E, F
			F -> D, E, G
			G -> A, F

		For this graph, BFS can work like following;
			A, B, C, E, G, D, F
			A, G, F, E, D, C, B

		Firstly, it look 'one' adjacent node of parent node, then look its adjacent node(Adjacent nodes of
		adjacent node of parent node). This DFS algorithm works as recursive. If node have been visited,
		DFS looks at the another adjacent node.

		:param node: Start node represents where the search start
		:return: Not return value
		"""
		if node.visited == False:
			node.visited = True
			print(node.name)

			[self.DFS_RECURSIVE(neighbour) for neighbour in node.adjacents]

	def DFS_ITERATIVE(self, start_node):
		"""
		DFS Algorithm; DFS searchs vertically on the graph/tree. This DFS uses stack as data structure.

		For example graph:
			A -> B, C, E, G
			B -> A
			C -> A
			D-> E, F
			F -> D, E, G
			G -> A, F

		For this graph, BFS can work like following;
			A, G, F, E, D, C, B

		Firstly, it look 'one' adjacent node of parent node, then look its adjacent node(Adjacent nodes of
		adjacent node of parent node). This DFS algorithm uses stack as data structure. If node have been visited,
		DFS receive last item of the stack, then begins to look at the another adjacent node.

		:param start_node: Start node represents where the search start
		:return: Not return value
		"""

		self._stack.push(start_node)
		while not self._stack.is_empty():
			current_node = self._stack.pop()
			if current_node.visited == False:
				current_node.visited = True
				print(current_node.name)

			[self._stack.push(neighbour) for neighbour in current_node.adjacents if neighbour.visited == False]

	def reset_all_nodes(self):
		for node in self.nodes:
			node.visited = False


# Example USAGE
# Create Nodes
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# Add adjacent nodes of all nodes
a.add_addjacents([b, e])
b.add_addjacents([a, d, c])
c.add_addjacents([b, d])
d.add_addjacents([b, c])
e.add_addjacents([a, f])
f.add_addjacents([e])

# Create graph, and add nodes to graph
graph = Graph()
graph.add_nodes([a, b, c, d, e, f])

# Run BFS on the graph
print("Visited Nodes with BFS: ")
graph.BFS(a)

graph.reset_all_nodes()

# Run Recursive DFS on the graph
print("Visited Nodes with Recursive DFS: ")
graph.DFS_RECURSIVE(a)

graph.reset_all_nodes()

# Run Iterative DFS on the graph
print("Visited Nodes with Iterative DFS: ")
graph.DFS_ITERATIVE(a)


