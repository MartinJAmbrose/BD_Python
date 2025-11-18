# Slicing Lists
def get_champion_slices(champions):
    champion_third = champions[2::]
    champion_notlast = champions[:-1]
    champion_even = champions[::2]
    return champion_third, champion_notlast, champion_even