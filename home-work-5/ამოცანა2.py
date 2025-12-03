'''
მოცემულია სია თანამშრომლების ლექსიკონებისა მათი სახელების, 3 დღის განმავლობაში
დავალებების რაოდენობის შესრულების, და მათი განყოფილებების მიხედვით:

employees = [
{"name": "Alice", "tasks": [5, 7, 9], "department": "IT"},
{"name": "Bob", "tasks": [2, 3, 4], "department": "Sales"},
{"name": "Charlie", "tasks": [8, 7, 6], "department": "IT"},
{"name": "Diana", "tasks": [9, 8, 10], "department": "Marketing"}
{"name": "George", "tasks": [2, 7, 6], "department": "IT"}
]

1) map და lambda ფუნქციების გამოყენებით შექმენით ლექსიკონების ახალი სია სადაც
თითოეული ლექსიკონის "name" და "department" იგივე იქნება,
ხოლო "tasks"-ის მაგივრად იქნება "average_tasks",
რომლის მნიშვნელობაშიც ეწერება დავალებების რაოდენობების საშუალო არითმეტიკული:

    [
        {"name": "Alice", "department": "IT", "average_tasks": 7},
        {…},
        {…}
    ]

2) sorted(…, key = lambda) გამოყენებით დაალაგეთ თანამშრომლები "average_tasks"-ის კლებადობის მიხედვით.

3) max(…, key = lambda)-ს გამოყენებით იპოვეთ ყველაზე მაღალი "average_tasks"-ის მქონე თანამშრომელი.

4) filter + lambda-ს გამოყენებით იპოვეთ IT განყოფილების თანამშრომლები, რომელთა "average_tasks" > 6.

'''

employees = [
{"name": "Alice", "tasks": [5, 7, 9], "department": "IT"},
{"name": "Bob", "tasks": [2, 3, 4], "department": "Sales"},
{"name": "Charlie", "tasks": [8, 7, 90], "department": "IT"},
{"name": "Diana", "tasks": [9, 8, 10], "department": "Marketing"},
{"name": "George", "tasks": [2, 7, 6], "department": "IT"},
{"name": "suxo", "tasks": [8, 7, 20], "department": "IT"}
]

employees_name_list = list(map(lambda names: names["name"], employees))
employees_tasks_list = list(map(lambda task: task["tasks"], employees))
employees_departments_list = list(map(lambda departament: departament["department"], employees))

new_dict1 = []

for i in range(len(employees_name_list)):
    average_tasks = (int((sum(employees_tasks_list[i])/len(employees_tasks_list[i]))))
    new_dict1.append({"name":employees_name_list[i], "average_tasks":average_tasks, "department": employees_departments_list[i]})

print("#####################################################################")
print("-------------------> თავდაპირველი არეული  <----------------------\n")

for i in new_dict1:
    print(i)

print("\n#####################################################################")
print("---> დაალაგებული თანამშრომლები average_tasks_ის კლებადობის მიხედვით <---\n")


sorted_employees = reversed(sorted(new_dict1, key=lambda x: x["average_tasks"]))

for i in sorted_employees:
    print(i)

print("#####################################################################")
print("--------> ყველაზე მაღალი average_tasks-ის მქონე თანამშრომელი <---------")

best_employees = max(new_dict1, key=lambda x: x["average_tasks"])
print("------------------------>", best_employees["name"],"<------------------------------")

'''
4) filter + lambda-ს გამოყენებით იპოვეთ IT განყოფილების თანამშრომლები, რომელთა "average_tasks" > 6.
'''
print("#####################################################################")
print("---> IT განყოფილების თანამშრომლები, რომელთა average_tasks > 6 <-------\n")

item = list(filter(lambda x: x['average_tasks'] > 6, new_dict1))
IT = list(filter(lambda x: x['department'] == "IT", item))

for item in IT:
    print(item["name"])
