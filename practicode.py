#Stop the loop if i is 3

# i = 0

# while i < 5:
#     print(f"i vale {i}")
#     i = i + 1
#     if i == 3:
#         break

#In the loop, when i is 3, jump directly to the next iteration.

# i = 0

# while i < 3:
#     print("i todavia vale menos que 3")
#     i += 1
#     if i == 3:
#         continue
#     print("i vale 3")

#Print a message once the condition is false.

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

#Loop through the items in the fruits list.

# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

"""
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

        
 


