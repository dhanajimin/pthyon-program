# python collection
# list tuple set dictionary

fruits=["apple","cherry","banana","mango"] 
print("list:", fruits)

#access list item (index)
print("access:",fruits[0])
print(fruits[1:3])
print(fruits[-1])

#change a item value
fruits[3]="orange"
print("change:",fruits)

#add list items
fruits.append("amla")
print("append:",fruits)

fruits.remove("apple")
print("remove:",fruits)

#remove specific item
fruits.pop(2)
print("pop:",fruits)

#to clear all ()
fruits.clear()
print()

#loop
fruits=["apple","banana","cherry","amla","mango"]
for x in fruits:
    print(x)
