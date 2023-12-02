import re

def string_to_number(string):
    if string == "one":
        return 1
    elif string == "two":
        return 2
    elif string == "three":
        return 3
    elif string == "four":
        return 4
    elif string == "five":
        return 5
    elif string == "six":
        return 6
    elif string == "seven":
        return 7
    elif string == "eight":
        return 8
    elif string == "nine":
        return 9
    else:
        return int(string)

sum_of_calibration_values = 0
with open("input.txt", "r") as calibration_document:
    for line in calibration_document:
        numerical_values = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        first_digit = numerical_values[0]
        last_digit = numerical_values[-1]
        sum_of_calibration_values += int(f"{string_to_number(first_digit)}{string_to_number(last_digit)}")

print(sum_of_calibration_values)