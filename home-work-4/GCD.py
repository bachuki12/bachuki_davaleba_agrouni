def gcd(a, b):
    copy_of_a = a
    copy_of_b = b
    while (b != 0):
            tmp = a % b
            a = b
            b = tmp
    return a

if __name__ == "__main__":
    copy_of_a = 12
    copy_of_b = 8
    print(f"LCM of {copy_of_a} and {copy_of_b} is {gcd(copy_of_a, copy_of_b)}.")