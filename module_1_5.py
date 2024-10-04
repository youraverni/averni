immutable_var = 1, 3, 4, "string", True, "string2", [1, 2, 3, 45]
print(immutable_var)
#нельзя изменить, вот так, фактически, кортеж можно изменить, если внутри есть список. Его также можно умножить и приплюсовать
immutable_var[6][2]= 81
print(immutable_var)
print(immutable_var * 3)
immutable_var1 = 0, 0, 0
print(immutable_var + immutable_var1)
mutable_list = [1, 3, 5, True, "string1"]
print(mutable_list)
mutable_list[0]= 81
mutable_list[3]= False
print(mutable_list)
