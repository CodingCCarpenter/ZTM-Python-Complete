some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup_free_list = [x for x in some_list if some_list.count(x) <= 1]
duplicates = {x for x in some_list if some_list.count(x) > 1}

print(list(duplicates))
print(dup_free_list)

