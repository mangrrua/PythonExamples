

class Stack:
    """
    Stack runs Last In First Out(LIFO)
    Item appended to top of the stack.
    If we want to pop item from the stack, remove top element of the stack.
    """

    def __init__(self):
        """
        Define items list for keep stack's items.
        """
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_top_element(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def sort(self):
        self.items.sort()

    def print_items(self):
        print("Items: {}".format(self.items))
