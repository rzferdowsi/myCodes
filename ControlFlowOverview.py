"""Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False"""
# Write your large_power function here:
def large_power(base,exponent):
  if base**exponent>5000:
    return True
  return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
"""Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.

The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise."""
# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < food_bill+ electricity_bill+ internet_bill+ rent:
    return True
  return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

"""Create a function named twice_as_large() that has two parameters named num1 and num2.

Return True if num1 is more than double num2. Return False otherwise."""
# Write your twice_as_large function here:
def twice_as_large(num1,num2):
  if num1 > 2*num2:
    return True
  return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

"""Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility."""
# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num%10==0:
    return True
  return False


# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

"""Create a function named not_sum_to_ten() that has two parameters named num1 and num2.

Return True if num1 and num2 do not sum to 10. Return False otherwise."""
# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
  if (num1 + num2 != 10):
    return True
  else:
    return False  
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

"""Create a function named in_range() that has three parameters named num, lower, and upper.

The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False."""

# Write your in_range function here:
def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

"""Create a function named same_name() that has two parameters named your_name and my_name.

If our names are identical, return True. Otherwise, return False."""

# Write your same_name function here:
def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

"""Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this."""
# Write your always_false function here:
def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

"""Create a function named movie_review() that has one parameter named rating.

If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!""""

# Write your movie_review function here:
def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

"""Create a function called max_num() that has three parameters named num1, num2, and num3.

The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!"."""

# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"


