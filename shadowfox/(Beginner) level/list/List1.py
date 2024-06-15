justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

number_of_members = len(justice_league)
print(f"Step 1: Number of members in the Justice League: {number_of_members}")

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(f"Step 2: After recruiting Batgirl and Nightwing: {justice_league}")

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"Step 3: Wonder Woman is now the leader: {justice_league}")

justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print(f"Step 4: After separating Aquaman and Flash: {justice_league}")

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"Step 5: New members of the Justice League: {justice_league}")

justice_league.sort()
print(f"Step 6: Justice League sorted alphabetically: {justice_league}")

new_leader = justice_league[0]
print(f"The new leader will be: {new_leader}")
