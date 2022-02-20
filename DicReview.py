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

"""Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys."""

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary): 
  l = []
  for key in my_dictionary:
    if my_dictionary[key] in list(my_dictionary.keys()):
      l.append(my_dictionary[key]) 
  return l
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

"""Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary."""

# Write your max_key function here:
def max_key(my_dictionary): 
  vl = list(my_dictionary.values())
  kl = list(my_dictionary.keys())
  maxv = max(vl)
  i = vl.index(maxv)
  return kl[i]
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

"""Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word."""

def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

"""Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words."""
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

"""Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary."""
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

"""Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

So in example above, the function would return:

{"S" : 4, "L": 3}"""
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

