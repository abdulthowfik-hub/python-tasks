print("\n---Question 1---")

i = 1

while i <= 10:
    print(i)
    i = i + 1

print("\n---Question 2---")

i = 10

while i >= 1:
    print(i)
    i = i - 1

print("\n---Question 3---")

i = 2

while i <= 50:
    print(i)
    i = i + 2

print("\n---Question 4---")

i = 1

while i <= 50:
    print(i)
    i = i + 2

print("\n---Question 5---")

n = 10
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print(sum)

print("\n---Question 6---")

num = 5
fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print(fact)

print("\n---Question 7---")

num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

print("\n---Question 8---")

num = 12345
num = 12345
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(sum)

print("\n---Question 9---")

num = 12345
count = 0

while num > 0:
    num = num // 10
    count = count + 1

print(count)

print("\n---Question 10---")

num = 121
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")