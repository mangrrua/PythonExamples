import Stack

stack = Stack.Stack()

# Print initial stack properties
print("-> Initial - Stack is empty: {}".format(stack.is_empty()))
print("-> Initial - Stack size: {}\n".format(stack.size()))

# Stack items states while push and pop
print("-> Instant states of Stack")
stack.print_items()

stack.push(8)
stack.print_items()

stack.push(32)
stack.print_items()

stack.push(73)
stack.print_items()

stack.pop()
stack.print_items()

stack.push(0)
stack.print_items()

stack.push(49)
stack.print_items()

stack.push(13)
stack.print_items()

stack.pop()
stack.print_items()

stack.push(4)
stack.print_items()

stack.push(16)
stack.print_items()

stack.push(35)
stack.print_items()

stack.push(21)
stack.print_items()

stack.pop()
stack.print_items()

# Stack's items after all push and pop operations
print("\n-> Before the items is sorted: ")
stack.print_items()

# Sort items of the Stack
stack.sort()

# Stack's items after sorted
print("\n-> After the items is sorted: ")
stack.print_items()
