#defining the business class
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
#defining the franchise class
class Franchise: 
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
#defining the menu class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  #menu items
  brunch_menu = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
  early_bird_menu = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 15.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
  dinner_menu = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00,}
  kids_menu = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}            

  brunch_menu = Menu('brunch', brunch_menu, 1100, 1600)  
  early_bird_menu = Menu('early_bird', early_bird_menu, 1500, 1800)
  dinner_menu = Menu('dinner', dinner_menu, 1700, 2300)
  kids_menu = Menu('kids', kids_menu, 1100, 2100)

  print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
  print(early_bird_menu.calculate_bill(['salumeria plate', 'vegan mushroom ravioli']))
#string representation
def __repr__(self):
  return self.name + 'menu available from ' + str(self.start_time) + ' - ' + str(self.end_time)
#print(brunch)

def calculate_bill(self, purchased_items):
  current_bill = 0
  for purcased_item in purchased_items:
    if items in self.items:
      current_bill += self.items[purcased_item]
  return current_bill

def __repr__(self):
    return self.address

def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

menus = {'brunch_menu', 'early_bird_menu', 'dinner_menu', 'kids_menu'}

flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

#print(flagship_store.available_menus(1200))
#print(flagship_store.available_menus(1700))

basta = Business("Basta fazoolin' with my heart", [flagship_store, new_installment])

arepas_menu = {'arepa pabllon': 7.00, 'pernill arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])
