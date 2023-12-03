from dataclasses import dataclass

@dataclass
class Place:
    is_empty: bool = False
    is_symbol: bool = False
    is_part: bool = False
    partnumber: int = 0

def has_numbers_above(x, y, places):
    y_above = y - 1
    x_above = x - 1
    numbers = set()
    for x_check in range(3):
        if y_above < 0 or y_above >= number_of_places_y:
            continue
        if x_above + x_check < 0 or x_above + x_check >= number_of_places_x:
            continue
        if places[y_above][x_above + x_check].is_part:
            numbers.add(places[y_above][x_above + x_check].partnumber)
    return numbers

def has_numbers_below(x, y, places):
    # Check below
    y_below = y + 1
    x_below = x - 1
    numbers = set()
    for x_check in range(3):
        if y_below < 0 or y_below >= number_of_places_y:
            continue
        if x_below + x_check < 0 or x_below + x_check >= number_of_places_x:
            continue
        if places[y_below][x_below + x_check].is_part:
            numbers.add(places[y_below][x_below + x_check].partnumber)
    return numbers

def has_number_left(x, y, places):
    # Check left
    y_left = y
    x_left = x - 1
    numbers = set()
    if y_left >= 0 and y_left < number_of_places_y and x_left >= 0 and x_left < number_of_places_x:
        if places[y_left][x_left].is_part:
            numbers.add(places[y_left][x_left].partnumber)
    return numbers

def has_number_right(x, y, places):
    # Check right
    y_right = y
    x_right = x + 1
    numbers = set()
    if y_right >= 0 and y_right < number_of_places_y and x_right >= 0 and x_right < number_of_places_x:
        if places[y_right][x_right].is_part:
            numbers.add(places[y_right][x_right].partnumber)
    return numbers
    

with open("input.txt", "r") as engine_schematic:
    number_of_places_x = 0
    number_of_places_y = 1
    line = engine_schematic.readline()
    number_of_places_x = len(line)
    for _ in engine_schematic:
        number_of_places_y += 1
    
    places = [[Place() for _ in range(number_of_places_x)] for _ in range(number_of_places_y)]
    engine_schematic.seek(0)

    for y, line in enumerate(engine_schematic):
        for x, char in enumerate(line):
            if char.isnumeric():
                places[y][x].is_part = True
                places[y][x].partnumber = char
                if x > 0 and places[y][x - 1].is_part:
                    new_partnumber = places[y][x - 1].partnumber + places[y][x].partnumber
                    partnumber_lenght = len(new_partnumber)
                    for i in range(partnumber_lenght - 1):
                        places[y][x - 1 - i].partnumber = new_partnumber
                    places[y][x].partnumber = new_partnumber

            elif char == "\n":
                pass
            elif char == "*":
                places[y][x].is_symbol = True
            else:
                places[y][x].is_empty = True
            

    partnumber_sum = 0
    for y in range(number_of_places_y):
        x = 0
        while x < number_of_places_x:
            if places[y][x].is_symbol:
                adjacent_numbers = set()
                adjacent_numbers.update(has_numbers_above(x, y, places))
                adjacent_numbers.update(has_numbers_below(x, y, places))
                adjacent_numbers.update(has_number_left(x, y, places))
                adjacent_numbers.update(has_number_right(x, y, places))
                if len(adjacent_numbers) == 2:
                    numbers = list(adjacent_numbers)
                    partnumber_sum += int(numbers[0]) * int(numbers[1])
                x += 1
            else:
                x += 1
    
    print(f"Sum of part numbers: {partnumber_sum}")




                    

                
