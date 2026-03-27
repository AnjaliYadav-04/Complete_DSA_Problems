''' ch = input("Enter a character: ")


if ch.lower() in ['a', 'e', 'i', 'o', 'u']:

    print("Vowel")

else:

    print("Not a Vowel")
'''


'''
ch = input("Enter a character: ")


if ch.lower() not in ['a', 'e', 'i', 'o', 'u']:

    print("consonants")

else:

    print("Not a consonants l")



num = int(input("Enter a number: "))


if num > 0:

    print("Positive")

else:

    print("Not Positive")





num = input("Enter value: ")


try:

    val = float(num)

    print("It is a number (float supported)")

except:

    print("Not a number")


num = float(input("Enter a number: "))


if isinstance(num, float):

    print("Float")





num = int(input("Enter a number: "))


if 100 <= num <= 999 or -999 <= num <= -100:

    print("3-digit number")

else:

    print("Not a 3-digit number")



s = input("Enter a string: ")


s = s.lower().replace(" ", "")


if s == s[::-1]:

    print("Palindrome")

else:

    print("Not Palindrome")






my_list = [10, 20, 30, 40, 50]  # Example list


if len(my_list) == 0:

    print("The list is empty, no middle value.")

else:

    mid_index = len(my_list) // 2

    if len(my_list) % 2 == 1:

        print(f"Middle value is: {my_list[mid_index]}")

    else:

        print(f"List has even length, middle values are: {my_list[mid_index-1]} and {my_list[mid_index]}")

'''


# Q) WAP to check whether last digit is 5 or not
'''num = int(input("Enter a number : "))
if num % 10 == 5:
    print("Yes, last digit is 5")
else:
    print("No, last digit is Not 5")'''


#Q) Print ASCII Value of a character only if it is Upper Case.
'''Name = input("Enter a character : ")
if 'A'<=Name<='Z':
    print("ASCII value is ",ord(Name))
else:
    print("Not an upper case char.")'''


# Q) WAP to print the cube of a number only if it is divisible by 9 or 6
'''num = int(input("Enter a number : "))
if num%9==0 or num%6==0:
    print(num**3)
else:
    print("Neighter divisible by 6 or 9")'''


# chech char is upper case, lower case, digit and special char
c = input("Enter a character : ")
if 'A'<=c<='Z':
    print("upper case")
elif 'a'<=c<='z':
    print("lower case")
elif '0'<=c<="9":
    print("digit")
else:
    print("Special char")