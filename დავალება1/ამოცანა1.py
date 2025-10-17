

#1) დაწერეთ პროგრამა, რომელიც მომხმარებელს მოსთხოვს სამკუთხედის გვერდების შეყვანას და ეკრანზე დაბეჭდავს მის ფართობს და პერიმეტრს.
import math

side_list = [0,0,0] # ვქმნით ლისტს სამკუთხედისთვის

cheshmariti =True


for i in range(len(side_list)):
    gvedri = int(input(f"შემოიტანეთ სამკუთხედის გვერდის სიგრძე "))  # მომხმარებლისგან ვიღებთ გვერდების სიგრძეს
    if gvedri<=0:
        break
    else:
        side_list[i] = gvedri

gverdi_1_plus_2 = side_list[0]+side_list[1]
gverdi_1_plus_3 = side_list[0]+side_list[2]
gverdi_2_plus_3 = side_list[1]+side_list[2]

if gverdi_1_plus_2 <= side_list[2] or gverdi_2_plus_3 <= side_list[0] or gverdi_1_plus_3 <= side_list[1]:
    print("ასეთი გვერდების მქონე სამკუთხედი არ არსებობს ")
else:
    perimetri =sum(side_list) # ვაჯამავთ ლისტის ელემენტებს
    s =  perimetri/2  #სამკუთხედის ფართობი გამოითვლება ფორმულით პრიმეტრი/2
    area =math.sqrt(s*((s-side_list[0])*(s-side_list[1])*(s-side_list[2])))

    print(f"სამკუთხედის პერიმეტრია ტოლია {perimetri}-სმ") #უბრალოდ ვბეჭდავთ სამკუთხედის პერიმეტრის მნიშვნელობას
    print(f"სამკუთხედის ფართობი ტოლია {area}-სმ²")  #უბრალოდ ვბეჭდავთ სამკუთხედის ფათობის მნიშვნელობას