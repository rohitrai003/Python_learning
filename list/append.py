lst = list()
list.append(lst, 1)
print(lst) # [1]
# or 
lst.append(1)
print(lst) # [1,1]
lst.append(2)
print(lst) # [1,1, 2]
lst.append(["John", "Cena"])
print(lst) # [1,1, 2, ["John", "Cena"]]

