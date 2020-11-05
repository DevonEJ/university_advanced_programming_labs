import sys
from converter import conversions


def run(convert_to, convert_from, convert_value):

        if convert_to == "celcius":
            result = conversions.to_celcius(convert_from, convert_value)
        if convert_to == "kilograms":
            result = conversions.to_kilograms(convert_from, convert_value)
        if convert_to == "metres":
            result = conversions.to_metres(convert_from, convert_value)
        if convert_to == "seconds":
            result = conversions.to_seconds(convert_from, convert_value)
        
        print(f"Result: {result}")



def main():

    target = ""

    while True:

        try:
            target = str(input("Please enter a unit to convert to (celcius, kilograms, metres or seconds (or exit)): "))

            if target == "exit":
                break

            unit = str(input("Please enter the unit you are converting from (hours, minutes, kelvin, feet, inches, or pounds): "))

            value = float(input("Please enter a numerical value to convert: "))

            assert target in ["celcius", "kilograms", "metres", "seconds"]
            assert unit in ["hours", "minutes", "kelvin", "feet", "inches", "pounds"]

        except Exception:
            sys.exit("Oops, read the options carefully!")

        run(target, unit, value)
    
    


if __name__ == "__main__":
    main()