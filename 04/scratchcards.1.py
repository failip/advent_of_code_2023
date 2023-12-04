with open("input.txt", "r") as scratchfile_pile:

    sum_of_points = 0

    for line in scratchfile_pile:
        _, line = line.split("Card")
        card_number, line = line.split(":")
        winning_numbers, your_numbers = line.split("|")
        winning_numbers = set(int(number) for number in winning_numbers.split())
        your_numbers = set(int(number) for number in your_numbers.split())
        right_numbers = winning_numbers.intersection(your_numbers)
        points = 0
        if right_numbers:
            points = 2 ** (len(right_numbers) - 1)
        sum_of_points += points
    
    print(sum_of_points)