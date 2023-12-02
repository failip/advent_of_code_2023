import re

sum_of_calibration_values = 0
with open("input.txt", "r") as calibration_document:
    for line in calibration_document:
        numerical_values = re.findall(r"\d", line)
        first_digit = numerical_values[0]
        last_digit = numerical_values[-1]
        sum_of_calibration_values += int(f"{first_digit}{last_digit}")

print(sum_of_calibration_values)