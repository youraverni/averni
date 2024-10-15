grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
grades_int= list(grades)

averages = []

for grade_list in grades:
    avg = sum(grade_list) / len(grade_list)
    averages.append(avg)

grades_zip = zip(students_list,averages)

grades_dict= dict(grades_zip)
print(grades_dict)
