
total_jumping_jacks = 100
jacks_per_set = 10

while total_jumping_jacks > 0:
    print(f"You have {total_jumping_jacks} jumping jacks remaining.")

    
    for _ in range(jacks_per_set):
        total_jumping_jacks -= 1
        if total_jumping_jacks == 0:
            break

    if total_jumping_jacks > 0:
        tired_response = input("Are you tired? (yes/no): ").lower()
        if tired_response == "yes" or tired_response == "y":
            skip_remaining_sets = input("Do you want to skip the remaining sets? (yes/no): ").lower()
            if skip_remaining_sets == "yes" or skip_remaining_sets == "y":
                break
        else:
            continue

if total_jumping_jacks == 0:
    print("Congratulations! You completed the workout.")
else:
    print(f"You completed a total of {100 - total_jumping_jacks} jumping jacks.")
