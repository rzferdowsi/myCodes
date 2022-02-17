"""Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.

We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function."""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def  unique_english_letters(word):
  unique_letters =[]
  count = 0
  for letter in word:
    if letter not in unique_letters:
       unique_letters.append(letter)
       count +=1
  return count

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
"""Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word."""
# Write your count_char_x function here:
def count_char_x(word, x):
  c=0
  for letter in word:
    if letter == x:
      c += 1 
  return c
    

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "p"))
# should print 1

"""Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long."""
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  return len(word.split(x))-1
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
"""Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

For example, substring_between_letters("apple", "p", "e") should return "pl"."""
# Write your substring_between_letters function here:
def substring_between_letters(word, start,end):
  if start in word and end in word:
    s = word.find(start)
    e = word.find(end)
    return word[s+1:e]
  else:
    return word
  
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "l", "e"))
# should print "apple"
print("__________")

def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  # print(start_ind)
  end_ind = word.find(end)
  # print(end_ind)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "l", "e"))
# should print "apple"
print("__________")

"""Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.

For example, the following three calls should all return True:"""

# Write your check_for_name function here:
def check_for_name(sentence, name):
  s = sentence.lower()
  n = name.lower()
  if n in s:
    return True
  return False
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

"""Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word."""

# Write your every_other_letter function here:
def every_other_letter(word):
   y = ""
   for i in range(len(word)):
     if i % 2 ==0:
       y +=word[i]
   return y
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 
"""secand way"""
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other


"""Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse."""


# Write your reverse_string function here:
def reverse_string(word):
  string = ""
  for i in range(len(word)):
    string += word[-(i+1)]
  return string  
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

"""Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space."""
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  nw1 = word2[0]+word1[1:]
  nw2 = word1[0]+word2[1:]
  return f"{nw1} {nw2}"
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

