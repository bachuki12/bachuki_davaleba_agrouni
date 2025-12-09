'''

დაწერეთ ფუნქცია, რომელსაც გადაეცემა ორი ზრდადობის მიხედვით
დალაგებული სია და დააბრუნებს ახალ სიას, რომელშიც ორივე სიის წევრები
იქნება დალაგებული მიმდევრობით. ფუნქციას დამატებით უნდა ჰქონდეს optional
პარამეტრი reverse, რომელიც ნაგულისხმევად უნდა იყოს False და ამ დროს
ფუნქცია ალაგებდეს წევრებს ზრდადობის მიხედვით. ხოლო True-ს გადაცემის
შემთხვევაში უნდა ალაგებდეს კლებადობის მიხედვით. არ გამოიყენოთ ფუნქციები sort და sorted.

მაგალითი 1:
გადავეცით [1, 3, 10] და [0, 4, 7, 9] - დააბრუნა [0, 1, 3, 4, 7, 9, 10].
მაგალითი 2 :
გადავეცით [1, 3, 10], [0, 4, 7, 9] და True - დააბრუნა [10, 9, 7, 4, 3, 1, 0].

'''

# Optimized Python program for implementation of Bubble Sort
def bubbleSort(masiv1, masiv2, one = False):
    arr = masiv1 + masiv2
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if one == True:
        arr.reverse()
    print("Sorted array:")
    print(arr)

# Driver code to test above
if __name__ == "__main__":
    masiv1 = [1, 3, -787]
    masiv2 = [0, 4, 7, 9]

    bubbleSort(masiv1, masiv2)
    bubbleSort(masiv1, masiv2, True)
