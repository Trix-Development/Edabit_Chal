# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

    # chickens = 2 legs
    # cows = 4 legs
    # pigs = 4 legs

# The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
def animals(chickens,cows,pigs):
  calc_chickens = chickens * 2
  calc_cows = cows * 4
  calc_pigs = pigs * 4
  return calc_chickens + calc_cows + calc_pigs

print(animals(5,2,8))