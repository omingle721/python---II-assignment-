# Create and Access List Elements
print("Create and Access List Elements")
my_list = [10, 20, 30, 40, 50]

print("List:", my_list)
print("First element:", my_list[0])
print("Third element:", my_list[2])
print("Last element:", my_list[-1])

Add and Remove List Elements
print("Add and Remove List Elements")

# Adding elements
my_list.append(60)       
my_list.insert(2, 25)  
print("After adding elements:", my_list)

# Removing elements
my_list.remove(30)        
popped = my_list.pop()    
print("Removed element using pop:", popped)
print("List after removing elements:", my_list)

# Sort List Elements
print("Sort List Elements")
my_list.sort()
print("Sorted List:", my_list)

# Reverse List Elements
print("Reverse List Elements")
my_list.reverse()
print("Reversed List:", my_list)