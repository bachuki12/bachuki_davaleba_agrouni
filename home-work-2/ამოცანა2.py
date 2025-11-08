#მოცემულია სტუდენტების ქულები ფიზიკაში, მათემატიკაში და ქიმიაში.
'''
    შექმენით და ეკრანზე გამოატანინეთ ლექსიკონი რომლის გასაღებებიც იქნება
სტუდენტის სახელები, ხოლო მნიშვნელობები ექნება ასევე ლექსიკონები, რომელთა
გასაღებები იქნება საგნის სახელები, და მნიშვნელობები - შესაბამისი ქულები.
Output: {'George': {'math': 85, 'physics': 90, 'chemistry': 80}, ...}
'''

subjects = {
'math': {'George': 85, 'Salome': 78, 'David': 92},
'physics': {'George': 90, 'David': 75, 'Salome': 88},
'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

name_and_grades = {}
sub_and_grades = {}
out_put = {}

subject_list = []
names_list = []

for key, value in subjects.items():
    name_and_grades.update(value)
    subject_list.append(key)

for names, grades in name_and_grades.items():
    names_list.append(names)
    sub_and_grades.update({subject_list[0]: name_and_grades.get(names)})
    sub_and_grades.update({subject_list[1]: name_and_grades.get(names)})
    sub_and_grades.update({subject_list[2]: name_and_grades.get(names)})

out_put.update({names_list[0]: sub_and_grades})
out_put.update({names_list[1]: sub_and_grades})
out_put.update({names_list[2]: sub_and_grades})
print(f"{out_put}\n")