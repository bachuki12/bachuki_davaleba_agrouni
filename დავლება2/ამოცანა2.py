'''
მოცემულია სტუდენტების ქულები ფიზიკაში, მათემატიკაში და ქიმიაში.
subjects = {
'math': {'George': 85, 'Salome': 78, 'David': 92},
'physics': {'George': 90, 'David': 75, 'Salome': 88},
'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}
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

# ახალი ლექსიკონი — result
result = {}

# საკვანძო ციკლები საგნებსა და სტუდენტებზე
for subject, students in subjects.items():
    for student, score in students.items():
        if student not in result:
            result[student] = {}
        result[student][subject] = score

print(result)
