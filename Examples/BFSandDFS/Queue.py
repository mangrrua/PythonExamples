class Queue:
    """
    Queue runs as FIFO(First In First Out)
    Item appended to head of the queue.
    If we want to pop item from the queue, remove first element of the queue.
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def sort(self):
        self.items.sort()

    def print_items(self):
        print("Items: {}".format(self.items))
