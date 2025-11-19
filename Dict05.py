# Create a new dictionary starting with the current inventory counts.
# Loop through each shipment dict and add quantities into the new dictionary.
# Loop through each sales dict and subtract quantities, keeping counts at a minimum of 0.
# Do not introduce new items from sales alone if they would be 0.
# Return the new dictionary.

def update_inventory(inventory, shipments, sales):

    result = inventory.copy()

    for shipment in shipments:
        for item, qty in shipment.items():
            result[item] = result.get(item, 0) + qty

    for sale in sales:
        for item, qty in sale.items():
            if item in result:
                result[item] = max(0, result[item] - qty)

    return result