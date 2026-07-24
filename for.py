# Print Natural Numbers up to n

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    print(i)

# Print Even Numbers up to n

n = int(input("Enter the value of n: "))

for i in range(2, n + 1, 2):
    print(i)

# Print Odd Numbers up to n

n = int(input("Enter the value of n: "))

for i in range(1, n + 1, 2):
    print(i) 

# Print the Series 1 2 4 8 16 32 ...

n = int(input("Enter the number of terms: "))

term = 1

for i in range(n):
    print(term)
    term = term * 2 

# Sum of the Series

n = int(input("Enter the value of n: "))

fact = 1
total = 1

for i in range(1, n + 1):
    fact = fact * i
    total = total + (1 / fact)

print("Sum =", total) 

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))

count = 0

for i in range(1, root + 1):
    if root % i == 0:
        count += 1

print("Square Root =", root)

if count == 2:
    print("Square Root is Prime")
else:
    print("Square Root is Not Prime")

