#2) დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს არა უდიდეს 1000-ის და ერთ ხაზზე დაბეჭდავს ამ რიცხვის ყველა გამყოფს.

ricxvi = int(input("შემოიტანე რაიმე ნატურარული რიცხვი (1-1000): "))
i = 1
gamyofebis_masivi = []
cheshmariti = True

while cheshmariti:
    if ricxvi <= 1000 and ricxvi > 0:
        if ricxvi%i==0:
            gamyofebis_masivi.append(i)
            i += 1
        else:
            i += 1
        if(ricxvi<i):
            cheshmariti = False
    else:
        ricxvi = int(input("რიცხვი უნდა იყოს 1-1000 შუალედში სცადეთ თავიდან: "))

print(f"{ricxvi}_ის გამყოფებია: -->", *gamyofebis_masivi, sep=" ")





