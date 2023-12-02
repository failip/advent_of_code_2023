from dataclasses import dataclass

def parse_pull_result(pull_result: str) -> tuple:
    red = 0
    green = 0
    blue = 0
    pulls = pull_result.split()
    for cube_index in range(0, len(pulls), 2):
        number_of_cubes = int(pulls[cube_index])
        cube_type = pulls[cube_index + 1]
        if cube_type == "red":
            red += number_of_cubes
        elif cube_type == "green":
            green += number_of_cubes
        elif cube_type == "blue":
            blue += number_of_cubes
        else:
            raise ValueError(f"Unknown cube type: {cube_type}")
    return red, green, blue

def pull_is_possible(red_cubes, green_cubes, blue_cubes) -> bool:
    max_red_cubes = 12
    max_green_cubes = 13
    max_blue_cubes = 14
    if red_cubes > max_red_cubes:
        return False
    elif green_cubes > max_green_cubes:
        return False
    elif blue_cubes > max_blue_cubes:
        return False
    else:
        return True

sum_of_possible_games = 0
with open("input.txt", "r") as game_document:
    game_results = []
    for line in game_document:
        line = line.replace(",", "")
        game_results = line.split()
        game_id = int(game_results[1][:-1])
        pulls = " ".join(game_results[2:])
        pull_results = pulls.split(";")
        game_is_possible = True
        for pull_result in pull_results:
            red, green, blue = parse_pull_result(pull_result)
            if not pull_is_possible(red, green, blue):
                game_is_possible = False
                break
        if game_is_possible:
            sum_of_possible_games += game_id

print(sum_of_possible_games)
        


        
        



