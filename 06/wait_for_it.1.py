with open("input.txt", "r") as race_file:
    times = [int(time) for time in race_file.readline().split()[1:]]
    distances = [int(distance) for distance in race_file.readline().split()[1:]]
    path_travelled = lambda race_time, hold_time: hold_time * (race_time - hold_time)
    total_win_conditions = 1
    for time, distance in zip(times, distances):
        win_conditions = 0
        for hold_time in range(time):
            distance_travelled = path_travelled(time, hold_time)
            if distance_travelled > distance:
                win_conditions += 1
        total_win_conditions *= win_conditions
    print(total_win_conditions)