'''პროგრამამ უნდა შეგვაყვანინოს წელიწადი და დაგვიბეჭდოს ნაკიანია თუ არა.
წელიწადი ნაკიანია თუ 400-ზე იყოფა, ან 4-ზე იყოფა მაგრამ 100-ზე არა. პროგრამამ
უნდა მოგთხოვოთ სწორი რიცხვის შეყვანა. მაგალითად, არანატურალური რიცხვის, ან
ციფრების გარდა სხვა სიმბოლოების შეყვანის შემთხვევაში თავიდან უნდა
მოგვთხოვოს რიცხვის შეყვანა.
'''


# შემეძლო ფუქციის გარეშეც დამეწერა უბრალოდ ასე გადავწყვიტე
def is_year_leap(year):
    return year != 0 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0

year = input("Enter any Year: :-) ")

while year.isdigit() == False or int(year) == 0:
        year = input("Your Enter Wrong Argument :-(\nPlease try Again: --> ")

year = int(year)

if is_year_leap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

