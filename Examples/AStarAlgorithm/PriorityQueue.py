import heapq

class PriorityQueue:
    """
    PriorityQueue provides keeps nodes with its priority.
    For example; if node has minimum f_cost, its priority is 0
    That is the first node to be released
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, node_with_costs, priority):
        heapq.heappush(self._queue, (priority, self._index, node_with_costs))
        self._index += 1

    def get_and_remove(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0
