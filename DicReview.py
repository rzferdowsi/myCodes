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
