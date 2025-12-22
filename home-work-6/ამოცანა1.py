'''
დაწერეთ პროგრამა რომელიც დაადგენს არის თუ არა გზა მიმართულ გრაფში ორ
წერტილს შორის. მიმართული გრაფი ნიშნავს რომ თუ გვაქვს გზა A → B, ეს არ ნიშნავს რომ
გვაქვს გზა B → A. სურათზე გამოსახულია გრაფის ლექსიკონი რომლის გასაღებებიდან
გზა გადის მისი მნიშვნელობის თითოეულ წევრთან. მაგალითად A → B და A → C.
 graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],

 }
თუ პროგრამას ვკითხავთ გზას A → E უნდა დააბრუნოს True რადგან შეგვიძლია A → C →
E გზით მივიდეთ. თუ პროგრამას ვკითხავთ გზას C→ D უნდა დააბრუნოს False.
შეადგინეთ ცოტა უფრო დიდი გრაფი და შეამოწმეთ თქვენი კოდის სისწორე მასზე
სხვდასხვა input-ისთვის.

'''

# ვქმნით გრაფს
graph = {
    'A': ['B', 'C', 'F', 'Z'],
    'B': ['J', 'K', 'C'],
    'C': ['E', 'V'],
}

def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return True

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if has_path(graph, neighbor, end, visited):
                return True

    return False

print(has_path(graph, 'A', 'C'))
print(has_path(graph, 'A', 'C'))

print(has_path(graph, 'A', 'L'))
print(has_path(graph, 'A', 'L'))

print(has_path(graph, 'A', 'C'))
print(has_path(graph, 'A', 'C'))
print()
print(has_path(graph, 'A', 'L'))
print(has_path(graph, 'A', 'V'))
print(has_path(graph, 'A', 'V'))
print(has_path(graph, 'A', 'L'))











