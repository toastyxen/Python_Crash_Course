# Empty list for storiing aliens
aliens = []

num_aliens = int(input("How many aliens do youn want? "))

# Make x Aliens based on input
for alien_number in range(num_aliens):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[0::3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

# Show the first 5 Aliens
for alien in aliens[:20]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
