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

"""Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary"""
# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary:
    my_dictionary[key] +=10
  return  my_dictionary 
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}
