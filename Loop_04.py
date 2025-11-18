# Continue Loops
def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        enchantment_strength = quest_number * 5
        counter += 1
        if counter < 3:
            continue    
        else:    
            counter = 0
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )


# Don't touch below this line


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")


def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)


main()