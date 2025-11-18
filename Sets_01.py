# Remove Dups in SETS
def remove_duplicates(spells):
 
    unique_spells = []
    for spell in spells:
        if spell not in unique_spells:
            unique_spells.append(spell)
            
 #   unique_spells = list(set(spells))  This is another way to do it
    
    return unique_spells