"""Carly's Clippers
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month."""
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
total_price = 0
for price in prices:
  total_price += price
print(f"total price haircut: {total_price}")
average_price = total_price/len(prices)
print(f"Average Haircut Price: {average_price}")
new_prices = [price-5 for price in prices]
print(f"this is new haircut price list: {new_prices}")
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_revenue = 0
for i in range(len(hairstyles)):
   total_revenue += prices[i]*last_week[i]
print(f"this is total revenue:{total_revenue}")
average_daily_revenue = total_revenue/7
print(f"average_daily_revenue is:{average_daily_revenue}")
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]
print(f"cut under $30: {cuts_under_30}")
