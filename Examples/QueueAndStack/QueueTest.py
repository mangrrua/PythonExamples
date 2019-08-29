import Queue

queue = Queue.Queue()

# Print initial queue properties
print("-> Initial - Queue is empty: {}".format(queue.is_empty()))
print("-> Initial - Queue size: {}\n".format(queue.size()))

# Queue items states while enqueue and dequeue
print("-> Instant states of Queue")
queue.print_items()

queue.enqueue(8)
queue.print_items()

queue.enqueue(32)
queue.print_items()

queue.enqueue(73)
queue.print_items()

queue.dequeue()
queue.print_items()

queue.enqueue(0)
queue.print_items()

queue.enqueue(49)
queue.print_items()

queue.enqueue(13)
queue.print_items()

queue.dequeue()
queue.print_items()

queue.enqueue(4)
queue.print_items()

queue.enqueue(16)
queue.print_items()

queue.enqueue(35)
queue.print_items()

queue.enqueue(21)
queue.print_items()

queue.dequeue()
queue.print_items()

# Queue's items after all enqueue and dequeue operations
print("\n-> Before the items is sorted: ")
queue.print_items()

# Sort items of the Queue
queue.sort()

# Queue's items after sorted
print("\n-> After the items is sorted: ")
queue.print_items()
