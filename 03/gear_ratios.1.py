from dataclasses import dataclass

@dataclass
class Place:
    is_empty: bool = False
    is_symbol: bool = False
    is_part: bool = False
    partnumber: int = 0

def has_symbol_above(x, y, places):
    y_above = y - 1
    x_above = x - 1
    for x_check in range(part_number_length + 2):
        if y_above < 0 or y_above >= number_of_places_y:
            continue
        if x_above + x_check < 0 or x_above + x_check >= number_of_places_x:
            continue
        if places[y_above][x_above + x_check].is_symbol:
            return True
    return False

def has_symbol_below(x, y, places):
    y_below = y + 1
    x_below = x - 1
    for x_check in range(part_number_length + 2):
        if y_below < 0 or y_below >= number_of_places_y:
            continue
        if x_below + x_check < 0 or x_below + x_check >= number_of_places_x:
            continue
        if places[y_below][x_below + x_check].is_symbol:
            return True
    return False

def has_symbol_left(x, y, places):
    y_left = y
    x_left = x - 1
    if y_left >= 0 and y_left < number_of_places_y and x_left >= 0 and x_left < number_of_places_x:
        if places[y_left][x_left].is_symbol:
            return True
    return False

def has_symbol_right(x, y, places):
    y_right = y
    x_right = x + part_number_length
    if y_right >= 0 and y_right < number_of_places_y and x_right >= 0 and x_right < number_of_places_x:
        if places[y_right][x_right].is_symbol:
            return True
    return False
    

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
            if char == ".":
                places[y][x].is_empty = True
            elif char.isnumeric():
                places[y][x].is_part = True
                places[y][x].partnumber = int(char)
            elif char == "\n":
                pass
            else:
                places[y][x].is_symbol = True


    partnumber_sum = 0
    for y in range(number_of_places_y):
        x = 0
        while x < number_of_places_x:
            if places[y][x].is_part:
                part_number_length = 1
                partnumber = f"{places[y][x].partnumber}"
                while places[y][x + part_number_length].is_part:
                    partnumber += f"{places[y][x + part_number_length].partnumber}"
                    part_number_length += 1
                partnumber = int(partnumber)
                if has_symbol_above(x, y, places):
                    partnumber_sum += partnumber
                elif has_symbol_below(x, y, places):
                    partnumber_sum += partnumber
                elif has_symbol_left(x, y, places):
                    partnumber_sum += partnumber
                elif has_symbol_right(x, y, places):
                    partnumber_sum += partnumber
                x += part_number_length
            else:
                x += 1
    
    print(f"Sum of part numbers: {partnumber_sum}")




                    

                
