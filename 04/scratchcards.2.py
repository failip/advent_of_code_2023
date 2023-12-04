with open("input.txt", "r") as scratchfile_pile:

    sum_of_points = 0
    copies = [0]

    for line in scratchfile_pile:
        _, line = line.split("Card")
        card_number, line = line.split(":")
        card_number = int(card_number)
        if card_number > len(copies):
            copies.append(0)
        copies[card_number - 1] += 1
        winning_numbers, your_numbers = line.split("|")
        winning_numbers = set(int(number) for number in winning_numbers.split())
        your_numbers = set(int(number) for number in your_numbers.split())
        right_numbers = winning_numbers.intersection(your_numbers)
        for extra_index in range(1, len(right_numbers) + 1):
            if card_number + extra_index > len(copies):
                copies.append(0)
            copies[card_number - 1 + extra_index] += copies[card_number - 1]
    
    print(sum(copies))