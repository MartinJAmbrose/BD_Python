# Nested Dictionary
def get_quest_status(progress):
    for k, v in progress.items():
        if k == "status":
            return v
        elif isinstance(v, dict):
            result = get_quest_status(v)
            if result is not None:
                return result
    return None
