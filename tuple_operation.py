# Create and access tuple
tuple1 = (10, 20, 30, 40, 50)

print("Tuple:", tuple1)
print("First element:", tuple1[0])
print("Third element:", tuple1[2])


# Nested Tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print("Nested Tuple:", nested_tuple)
print("Access element from nested tuple:", nested_tuple[1][2])


# Repetition of Tuple
tuple_repeat = tuple1 * 2
print("Repeated Tuple:", tuple_repeat)


# Concatenation of Tuples
tuple2 = (60, 70, 80)

concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)