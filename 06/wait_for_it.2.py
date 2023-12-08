with open("input.txt", "r") as race_file:
    time = int("".join(race_file.readline().split()[1:]))
    distance = int("".join(race_file.readline().split()[1:]))
    path_travelled = lambda race_time, hold_time: hold_time * (race_time - hold_time)
    win_conditions = 0
    for hold_time in range(time):
        distance_travelled = path_travelled(time, hold_time)
        if distance_travelled > distance:
            win_conditions += 1
    print(win_conditions)