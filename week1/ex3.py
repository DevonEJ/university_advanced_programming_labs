
import sys


def get_user_input():
    try:
        days = int(input("Please enter how many days in the month: "))
        start = int(input("Which day 1-7 (Mon-Sun) does the week start on? "))
    except Exception:
        sys.exit("Oops, try again! Make sure you enter numbers only.")
    return days, start


def generate_calendar(num_days, week_start):

    days = "M   T   W  Th   F   S  Su"

    current_days = []

    # Initialise starting day
    current_days = current_days + (['    '] * (week_start - 1))

    print(days)
    # Initialise counter to keep track of lines printed - set to 1 to account for day names
    counter = 1

    for day in range(1, num_days + 1):
        if len(str(day)) == 2:
            spaces = '  '
        elif len(str(day)) == 1:
            spaces = '   '
        current_days.append(str(day) + spaces)
        if len(current_days) % 7 == 0:
            counter += 1
            print(''.join(current_days))
            current_days = []   
            print()
        elif day == num_days:
            counter += 1
            print(day)
    if counter < 7:
        print()


def main():
    days, start = get_user_input()
    generate_calendar(days, start)



if __name__ =="__main__":
    main()



