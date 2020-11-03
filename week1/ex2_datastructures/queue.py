# LIFO Stack

# Initialise variables
instruction = ""
queue = []

while instruction != "exit":

    instruction = str(input("Pick an operation: push, pop, or view (or type exit): ")).strip()

    if instruction == "push":
        item = str(input("Enter the value to push on to the end of the queue: ")).strip()
        queue.append(item)
    elif instruction == "pop":
        if len(queue) > 0:
            print("This value was popped off the queue: ", queue.pop(0))
        else:
            print("Oops, this queue is empty - try pushing a value on to it before popping!")
    elif instruction == "view":
        if len(queue) > 0:
            print("Here is the queue: ", queue)
        else:
            print("Oops, this queue is empty - try pushing a value on to it before viewing!")