"""Len's Slice
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data."""

# Your code below:
toppings = ["pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"]
prices = [2,
6,
1,
3,
2,
7,
2]
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)
num_pizzas=len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")
# print("We sell", num_pizzas, "different kinds of pizza!")
# print("We sell"+ " "+str(num_pizzas)+ " "+ "different kinds of pizza!")
pizza_and_prices =[[prices[0],toppings[0]],[prices[1],toppings[1]],[prices[2],toppings[2]],[prices[3],toppings[3]],[prices[4],toppings[4]],[prices[5],toppings[5]],[prices[6],toppings[6]]]
pizza_and_prices_p =f"""{prices[0]} {toppings[0]}\n{prices[1]} {toppings[1]}\n{prices[2]} {toppings[2]}\n{prices[3]} {toppings[3]}\n{prices[4]} {toppings[4]}\n{prices[5]} {toppings[5]}\n{prices[6]} {toppings[6]}"""
# pizza_and_prices = [[prices[i],toppings[i]] for i in range(0,7)]
print(pizza_and_prices)
pizza_and_prices.sort()

print(pizza_and_prices)
print(pizza_and_prices_p)
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# pizza_and_prices.remove([7, 'anchovies'])
pizza_and_prices.pop(len(pizza_and_prices)-1)
print(pizza_and_prices)
pizza_and_prices.insert(4,[2.5, "peppers"])
print(pizza_and_prices)
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
# i=toppings.index("cheese")
# print(i)
# pi=prices[i]
# print(pi)
