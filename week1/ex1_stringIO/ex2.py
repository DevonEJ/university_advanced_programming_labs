import sys


def main():
    try:
        requested_table = int(input(f"Hello! Which multiplication table would you like to see? "))
    except Exception:
        sys.exit("Oops - make sure you enter a number!")

    for num in range(1, (requested_table + 1)):
        if num % 2 == 0:
            print(f"{requested_table} times {str(num)} is {requested_table * num}")



if __name__ =="__main__":
    main()
