first = int(input("Введите 1 число:"))
second = int(input("Введите 2 число:"))
third = int(input("Введите 2 число:"))
print(first,second,third)
if first == second == third:
    print("Между собой равны 3 числа")
elif first == second or second == third or third == first:
    print("Между собой равны 2 числа")
elif first != second or second != third or third != first:
    print("Нет совпадающих числел")