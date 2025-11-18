# Raise and Exception
def purchase_item(price, gold_available):
    result = gold_available - price
    if result < 0:
        raise Exception("not enough gold")
    else:
        return result
