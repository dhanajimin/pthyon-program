# python string format

price = 150
txt = "the price is {} rupee"
print(txt.format(price))

#float
price = 150 
txt = "the price is {:.2f} rupee"
print(txt.format(price))

#multiple values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#index numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))



