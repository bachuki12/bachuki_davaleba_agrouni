'''
დაწერეთ პროგრამა რომელიც მომხმარებლის შემოყვანილ ტექსტს დაშიფრავს ან
განშიფრავს და დაბეჭდავს ეკრანზე. ნებისმიერი სიმბოლო რომელიც არ მიეკუთვნება
a-z დატოვეთ უცვლელი.
დაშიფვრის ლოგიკა ასეთია: ყოველი დაბალი რეგისტრის სიმბოლო (a-z) უნდა
შეიცვალოს კლავიატურაზე მის მარჯვნივ მდგომი სიმბოლოთი. თუ სიმბოლოს
მარჯვნივ კლავიატურაზე ინგლისური სიმბოლო არ არის, მაშინ უნდა გადავიდეს
პირველ სიმბოლოში ამ სტრიქონიდან. მაგალითად: p -> q, l -> a და ა.შ. პროგრამამ
უნდა გარდაქმნას მხოლოდ დაბალი რეგისტრის ინგლისური ასოები a-z, ხოლო
ყველა დანარჩენი სიმბოლო შეუცვლელი დატოვოს.
განშიფვრის ლოგიკა არის ზემოთ აღწერილი დაშიფვრით მიღებული ტექსტის
აღდგენა, ანუ მისი შებრუნებული პროცესი.
პროგრამამ ტექსტის გარდა უნდა მოგვთხოვოს e ან d-ს შეყვანა, სადაც e ნიშნავს
დაშიფვრის ბრძანებას, ხოლო d ნიშნავს განშიფვრის ბრძანებას. სხვა სიმბოლოს
შეყვანის შემთხვევაში მოგვთხოვოს თავიდან შეყვანა.

მაგ. 1:
Enter action (e/d): e
Enter text: power IS THE power
qpert IS THE qpert
მაგ. 2:
Enter action (e/d): d
Enter text: quyjpm IS COOL
python IS COOL

'''



q_p= 'qwertyuiop'
a_l ='asdfghjkl'
z_m= 'zxcvbnm'

input_text = input("Enter text: ")
action = input("Enter action (e/d): ")

def e():
    output_text = ""
    for i in input_text:
        if i in q_p:
            text_index = (q_p.index(i)%9)+1
            output_text += q_p[text_index]
        elif i in a_l:
            text_index = (a_l.index(i)%8)+1
            output_text += a_l[text_index]
        elif i in z_m:
            text_index = (z_m.index(i)%6)+1
            output_text += z_m[text_index]
        else:
            output_text += i
    print(F"{input_text} --> {output_text}")

def d():
    output_text = ""
    for i in input_text:
        if i in q_p:
            text_index = q_p.index(i)-1
            output_text += q_p[text_index]
        elif i in a_l:
            text_index = a_l.index(i)-1
            output_text += a_l[text_index]
        elif i in z_m:
            text_index = z_m.index(i)-1
            output_text += z_m[text_index]
        else:
            output_text += i
    print(F"{input_text} --> {output_text}")

while True:
    if action == 'e':
        e()
        break
    elif action == 'd':
        d()
        break
    else:
        action = input("Enter correct action (e/d): ")
        input_text = input("Enter text: ")