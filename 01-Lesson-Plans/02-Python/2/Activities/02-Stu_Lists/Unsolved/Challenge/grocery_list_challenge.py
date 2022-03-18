# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries

groceries= ["Water","Butter","Eggs","Apples","Cinnamon","Sugar", "Milk"]

print(groceries)


# @TODO: Find the first two items on the list

print(groceries[0:2])

# @TODO: Find the last five items on the list

print(groceries[2:7])

# @TODO: Find every other item on the list, starting from the second item
print(groceries[1::2])



# @TODO: Add an element to the end of the list

groceries.append("lettuce")
print(groceries)



# @TODO: Changes a specified element within the list at the given index

groceries [6]= ("Cream")
print(groceries)



# @TODO: Calculate how many items you have in the list
print(len(groceries))



# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name
index= groceries.index("Apples")
print(index)




# @TODO: Remove an element from the list based on the given element name

groceries.remove("lettuce")
print(groceries)


# @TODO: Remove an element from the list based on the given index
del groceries [0]
print(groceries)





# @TODO: Remove the last element of the list
del groceries [-1]
print(groceries)



print("You continue on your journey purchasing groceries...")
