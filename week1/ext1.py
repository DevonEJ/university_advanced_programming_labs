import sys


def get_user_input():
    try:
        diagram_mode = str(input(f"Would you like a right triangle, left triangle, or diamond? Enter R, L, or D: ") ) 
        num_symbols = int(input("How many symbols do you want it to use? Enter a number: "))
        type_symbol = str(input("Which symbol do you want it to use? Enter a symbol: "))

        assert diagram_mode in ["R", "L"]

    except Exception:
        sys.exit(f"Oops, read the input instructions carefully and try again...")
    return diagram_mode, num_symbols, type_symbol


def produce_diagram(mode, num_symbols, symbol):
    for i in range(1, num_symbols+1):  
        for _ in range(1, i+1):
            stars = i * symbol
            if mode == "R":
                spaces = (num_symbols - i) * " "
            else:
                spaces = ""
        print(spaces + stars, end="")     
        print()


def main(): 
    diagram, num_syms, sym_type = get_user_input()

    produce_diagram(diagram, num_syms, sym_type)
    

if __name__ =="__main__":
    main()


