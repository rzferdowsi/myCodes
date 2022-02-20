"""Write a function named tenth_power() that has one parameter named num.

The function should return num raised to the 10th power."""
def tenth_power(num):
  return num ** 10

"""Write a function named square_root() that has one parameter named num.

Use exponents (**) to return the square root of num."""
def square_root(num):
  return num ** 0.5

"""Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers."""

def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100

"""Write a function named average() that has two parameters named num1 and num2.

The function should return the average of these two numbers."""

def average(num1, num2):
  return (num1 + num2) / 2

"""Write a function named remainder() that has two parameters named num1 and num2.

The function should return the remainder of twice num1 divided by half of num2."""

def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

"""Write a function named first_three_multiples() that has one parameter named num.

This function should print the first three multiples of num. Then, it should return the third multiple.

For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21."""

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

"""Create a function called tip() that has two parameters named total and percentage.

This function should return the amount you should tip given a total and the percentage you want to tip."""
def tip(total, percentage):
  tip_amount = (total * percentage) / 100
  return tip_amount
"""Write a function named introduction() that has two parameters named first_name and last_name.

The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name."""

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

"""Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

The function should compute the age in dog years and return the following string:

"{name}, you are {age} years old in dog years"
Test this function with your name and your age!"""

def dog_years(name, age):
  return name+", you are "+str(age * 7)+" years old in dog years"

"""Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.

First, print the sum of a and b.

Second, print c minus d.

Third, print the first number printed, multiplied by the second number printed.

Finally, return the third number printed modulo a."""

def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth


