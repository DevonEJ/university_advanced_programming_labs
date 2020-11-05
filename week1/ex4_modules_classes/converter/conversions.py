

def to_metres(unit, value):
    if value > 0:
        if unit == "feet":
            divisor = 3.2808
        elif unit == "inches":
            divisor = 39.370
        else:
            raise Exception(f"to_metres does not recognise measurement unit: {unit}. Use inches or feet only.")
        metres = value /divisor
        return metres
    else:
        return 0


def to_kilograms(unit, value):
    if value > 0:
        if unit == "pounds":
            kg = value * 2.2046
            return kg
        else:
            raise Exception(f"to_kilogramgs does not recognise measurement unit: {unit}. Use pounds only.")
    else:
        return 0


def to_celcius(unit, value):
    if value > 0:
        if unit == "kelvin":
            celcius = value - 273.15
            return celcius
        else:
            raise Exception(f"to_celcius does not recognise measurement unit: {unit}. Use kelvin only.")
    else:
        raise Exception(f"to_celcius cannot convert a value of: {value}. Must be above 0.")


def to_seconds(unit, value):
    if value > 0:
        if unit == "hours":
            seconds = value * 3600
        elif unit == "minutes":
            seconds = value * 60
        else:
            raise Exception(f"to_seconds does not recognise measurement unit: {unit}. Use hours or minutes only.")
        return seconds
    else:
        return 0
