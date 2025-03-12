def pos_only(l):
    new_list = []
    for element in l:
        if element > 0:
            new_list.append(element)
    return new_list

lis=[-3, -2, -1, 0, 1, 2, 3]
print(pos_only(lis))

