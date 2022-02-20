"""Basta Fazoolin'
You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video."""

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"
  def calculate_bill(self,purchased_items): 
    bill=0
    for item in purchased_items:
      if item in self.items:
        v = self.items[item]
        bill += v
      else:
        print(f"'{item}' is not in the menu")
    # print("Bill:",bill)
    return bill 

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus 
  def __repr__(self):
    return self.address 
  def available_menus(self,time):
    available_menu=[]
    for menu in self.menus:
      if menu.start_time < time < menu.end_time:
        available_menu.append(menu.name)
    return available_menu

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return f'The business name is "{self.name}"\nThe franchieses are located in {(self.franchises)}' 

#Test Menu
brunch = Menu("brunch",{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50,
 'orange juice': 3.50},11,16)
print(brunch,"\n-----------")
print(brunch.items)
Brunch_Bill = brunch.calculate_bill(["pancakes","ice tea","home fries","coffee"])
print("Brunch Bill: $",Brunch_Bill)
print("__________________________")

early_bird = Menu("early_bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},15 ,18)
print(early_bird)
print(early_bird.items)
Early_bird_Bill = early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)'])
print("Early bird Bill: $",Early_bird_Bill)
print("__________________________")

dinner = Menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},17, 23)
print(dinner)
print(dinner.items)
print("__________________________")

kids = Menu("kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11 ,21)
print(kids)
print(kids.items)
print("__________________________")

arepas_menu = Menu("Take a’ Arepa",{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},10,20)

# Test Franchise    
flagship_store = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))
print("__________________________")
new_installment =Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])
print(new_installment)

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])
print("__________________________")
print("__________________________")
basta= Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
print(basta.franchises[0].menus[2])
print("__________________________")
print(Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment]))
print("__________________________")
print(Business("Take a' Arepa", [arepas_place]))



