with open("input.txt", "r") as oasis_and_sand_instability_sensor_data:
    total_sum_of_new_elements = 0
    for line in oasis_and_sand_instability_sensor_data:
        history = [int(value) for value in line.split()]
        derivatives = [[history[i] - history[i - 1] for i in range(1, len(history))]]
        while any(derivatives[-1]):
            derivatives.append([derivatives[-1][i] - derivatives[-1][i - 1] for i in range(1, len(derivatives[-1]))])
            
        new_element = 0
        for derivate in reversed(derivatives):
            new_element = derivate[0] - new_element 

        new_element = history[0] - new_element
        total_sum_of_new_elements += new_element
    print(total_sum_of_new_elements)
