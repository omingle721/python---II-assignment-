# Create sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Create and access set elements
print("Set 1:", set1)
print("Set 2:", set2)

print("Accessing elements of Set 1:")
for element in set1:
    print(element)

#  Union of the elements
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection of the elements
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)