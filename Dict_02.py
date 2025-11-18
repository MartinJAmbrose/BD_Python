# Iterating over a dictionary
def get_most_common_enemy(enemies_dict):
    valid_data = {k: v for k, v in enemies_dict.items() if v is not None}
    if not valid_data:
        return None
    highest = max(valid_data, key=valid_data.get)
    return highest
        