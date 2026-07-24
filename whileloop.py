# Print Natural Numbers up to n

n = int(input("Enter the value of n: "))

i = 1
while i <= n:
    print(i)
    i += 1

# Print Even Numbers up to n

n = int(input("Enter the value of n: "))

i = 2
while i <= n:
    print(i)
    i += 2

# Print Odd Numbers up to n

n = int(input("Enter the value of n: "))

i = 1
while i <= n:
    print(i)
    i += 2

# Sum of Natural Numbers up to n

n = int(input("Enter the value of n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i += 1

print("Sum =", sum) 

# Sum of Odd Numbers up to n

n = int(input("Enter the value of n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i += 2

print("Sum of Odd Numbers =", sum)

# Sum of Even Numbers up to n

n = int(input("Enter the value of n: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i += 2

print("Sum of Even Numbers =", sum)

# Print Natural Numbers in Reverse Order

n = int(input("Enter the value of n: "))

i = n

while i >= 1:
    print(i)
    i -= 1

# Fibonacci Series up to n Terms

n = int(input("Enter the number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1   

# Factorial of a Given Number

n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)    