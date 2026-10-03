print("\n---Question 1---")

for i in range(1, 11):
    print(i)

print("\n---Question 2---")

for i in range(10, 0, -1):
    print(i)

print("\n---Question 3---")

for i in range(2, 51, 2):
    print(i)

print("\n---Question 4---")

for i in range(1, 51, 2):
    print(i)

print("\n---Question 5---")

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\n---Question 6---")

sum = 0

for i in range(1, 101):
    sum = sum + i

print(sum)

print("\n---Question 7---")

sum = 0

for i in range(2, 51, 2):
    sum = sum + i

print(sum)

print("\n---Question 8---")

sum = 0

for i in range(1, 51, 2):
    sum = sum + i

print(sum)

print("\n---Question 9---")

for i in range(1, 11):
    print(i * i)

print("\n---Question 10---")

for i in range(1, 11):
    print(i * i * i)

print("\n---Question 11---")

num = 3
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(fact)

print("\n---Question 12---")

num = 12345
count = 0

for i in str(num):
    count = count + 1

print(count)

print("\n---Question 13---")

num = 12345
sum = 0

for i in str(num):
    sum = sum + int(i)

print(sum)

print("\n---Question 14---")

num = 12

for i in range(1, num + 1):
    if num % i == 0:
        print(i)

print("\n---Question 15---")

num = 7
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")

print("\n---Question 16---")

for num in range(2, 101):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)

print("\n---Question 17---")

numbers = [10, 25, 5, 40, 15]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest)

print("\n---Question 18---")

numbers = [10, 25, 5, 40, 15]
smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print(smallest)

print("\n---Question 19---")

numbers = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even)
print("Odd =", odd)

print("\n---Question 20---")

numbers = [10, -5, 0, 8, -2, 0, 4]
positive = 0
negative = 0
zero = 0

for i in numbers:
    if i > 0:
        positive = positive + 1
    elif i < 0:
        negative = negative + 1
    else:
        zero = zero + 1

print("Positive =", positive)
print("Negative =", negative)
print("Zero =", zero)