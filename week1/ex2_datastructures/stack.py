# LIFO Stack



# Initialise variables
instruction = ""
stack = []

while instruction != "exit":

    instruction = str(input("Pick an operation: push, pop, or view (or type exit): ")).strip()

    if instruction == "push":
        item = str(input("Enter the value to push on to the stack: ")).strip()
        stack.append(item)
    elif instruction == "pop":
        if len(stack) > 0:
            print("This value was popped off the stack: ", stack.pop())
        else:
            print("Oops, this stack is empty - try pushing a value on to it before popping!")
    elif instruction == "view":
        if len(stack) > 0:
            # Format the stack in an intuitive visual
            temp_stack = stack.copy()
            temp_stack.reverse()
            print("Here is the stack: ", *temp_stack, sep = "\n")
        else:
            print("Oops, this stack is empty - try pushing a value on to it before viewing!")

        




