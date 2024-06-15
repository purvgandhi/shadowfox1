import random
count_6 = 0
count_1 = 0
count_two_6s_in_row = 0
previous_roll = None

for _ in range(20):
    roll = random.randint(1, 6)
    print(f"Roll: {roll}")

    if roll == 6:
        count_6 += 1

   
    if roll == 1:
        count_1 += 1

    if roll == 6 and previous_roll == 6:
        count_two_6s_in_row += 1


    previous_roll = roll

# Print statistics
print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {count_two_6s_in_row}")
