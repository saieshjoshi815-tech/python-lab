# Check Whether Number is Zero or Non-Zero

n = int(input("Enter a number: "))

if n == 0:
    print("The number is Zero")
else:
    print("The number is Non-Zero")

# Find the Largest of Two Numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print("Largest Number =", a)
else:
    print("Largest Number =", b)

# Whether Number is Positive or Negative

n = int(input("Enter a number: "))

if n > 0:
    print("The number is Positive")
elif n < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# Whether Character is Vowel or Consonant

ch = input("Enter a Character: ")

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
   ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("It is a Vowel")
else:
    print("It is a Consonant")        

# Check Whether a Number is Even or Odd

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")    

# Check Whether a Year is Leap Year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")    