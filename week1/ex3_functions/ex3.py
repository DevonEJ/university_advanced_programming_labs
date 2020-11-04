import sys


def push(structure, data_structure):
    item = str(input(f"Enter the value to push on to the {structure}: ")).strip()
    data_structure.append(item)
    return data_structure


def pop(structure, data_structure):
    if len(data_structure) > 0:
        if structure == "queue":
            print(f"This value was popped off the {structure}: ", data_structure.pop(0))
        else:
            print(f"This value was popped off the {structure}: ", data_structure.pop())
    else:
        print(f"Oops, this {structure} is empty - try pushing a value on to it before popping!")
    return data_structure


def view(structure, data_structure):
    if len(data_structure) > 0:
        if structure == "queue":
            print(f"Here is the {structure}: ", data_structure)
        else:
            # Format the stack in an intuitive visual
            temp_stack = data_structure.copy()
            temp_stack.reverse()
            print("Here is the stack: ", *temp_stack, sep = "\n")
    else:
        print(f"Oops, this {structure} is empty - try pushing a value on to it before viewing!")


def main():
    data_structure = []
    instruction = ""

    try:
        structure = str(input("Pick an operation: stack or queue (or type exit): ")).strip()
        assert structure in ["stack", "queue"]
    except Exception:
        sys.exit("Oops, try again, make sure you only type stack or queue!")
    
    while instruction != "exit":

        instruction = str(input("Pick an operation: push, pop, or view (or type exit): ")).strip()

        if instruction == "push":
            data_structure = push(structure, data_structure)
        elif instruction == "pop":
            data_structure = pop(structure, data_structure)
        elif instruction == "view":
            view(structure, data_structure)


if __name__ =="__main__":
    main()