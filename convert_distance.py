def convert_distance(distance, unit):
    if unit == "km":
        return distance * 111.12
    elif unit == "miles":
        return distance * 69.046766881413
    elif unit == "nm":
        return distance * 60
    else:
        raise ValueError("Invalid unit. Supported units are 'km', 'miles', and 'nm'.")
