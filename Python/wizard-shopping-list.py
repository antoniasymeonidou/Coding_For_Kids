list = ['frog legs', 'bat eye', 'butterfly wing', 'pig ear']
print(list)

# Change list items
list[2] = 'magic sprinkles'
print(list)

# Add item to the list
list.append('scary tail')
print(list)
list.append('tongue')
print(list)

# Amount of items inside the list
amount = len(list)
print(amount)

# Delete item from the list
del list[0]
print(list)

# Sort List
list.sort()
print(list)

# This will return the items from position 2 to 3
print(list[2:3])

# Lowercase list
list.sort(key = str.lower)
print(list)

# Loop 1
for x in list:
  print(x)
  
# Join lists
list2 = ['blue water', 'sun smile', 'finger']
list3 = list + list2
print(list3)

or

list.extend(list2)
print(list)
 
