"""Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary"""
# Write your sum_values function here:
def sum_values(my_dictionary):
  l= list(my_dictionary.values())
  s = 0
  for i in l:
    s += i
  return s 
# Uncomment these function calls to test your sum_values function:

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

"""Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys."""

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  s = 0
  for key in my_dictionary:
    if key % 2 == 0:
      s+= my_dictionary[key]
  return s
   
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6
