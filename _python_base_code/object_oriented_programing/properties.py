# read only attribute
#walidacja gettery settery do zmainy danych w trakcie kodu
# %%
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed) #False
pizza.pineapple_allowed = True #AttributeError: can't set attribute
# %% funkcja setter - ustawiająca, getter - pobierająca
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False
  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed
  @pineapple_allowed.setter #funkcja ustawiająca
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "haslo":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
# %%

# %%
