# if we want to copy one list into another list
animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals
large_cats.append("Tiger")
print(animals)

# animals and large_cats now refer to the same list. how can we have different list?
#USING SLICING approach

large_catss = animals
large_catss = animals[:]
large_catss.append("leopard")
print(large_catss)
print(animals)
