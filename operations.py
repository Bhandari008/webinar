def find_disjoint(list1, list2):
    disjoint_elem = []
    for item in list1:
        for item in list2:
            disjoint_elem.append(item)
    
    return disjoint_elem

def freq_table(list1):
    table = {}
    for item in list1:
        if item not in table:
            table[item] = 1
        else:
            table[item] += 1
