print("\n---Question 1---")

string="python"
print(string)

print("\n---Question 2---")

name="Abdul"
print(name)

print("\n---Question 3---")

string="python"
print(len(string))

print("\n---Question 4---")

string="python"
print(string[0])

print("\n---Question 5---")

string="python"
print(string[-1])

print("\n---Question 6---")

string="python"
print(string.upper())

print("\n---Question 7---")

string="python"
print(string.lower())

print("\n---Question 8---")

string="python"
print(string[::-1])

print("\n---Question 9---")

string="python"
print(string[:3])

print("\n---Question 10---")

string="python"
print(len(string))

print("\n---Question 11---")

try:
    a=10
    b=0
    print(a/b)
except:
    print("Cannot divide by zero")

print("\n---Question 12---")

try:
    a = 20
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("\n---Question 13---")

try:
    number = int("abc")
    print(number)
except ValueError:
    print("Invalid input")

print("\n---Question 14---")

try:
    a = 10
    b = 2
    print(a / b)
except:
    print("An error occurred")
finally:
    print("Program completed")

print("\n---Question 15---")

try:
    number = int("hello")
    print(number)
except ValueError:
    print("Cannot convert string into integer")

print("\n---Question 16---")

try:
    a = int("10")
    b = int("20")
    print(a + b)
except ValueError:
    print("Invalid input")

    print("\n---Question 17---")

import copy

list1 = [1, 2, 3]
list2 = copy.copy(list1)

print(list2)

print("\n---Question 18---")

import copy

list1 = [10, 20, 30]
list2 = copy.copy(list1)

print(list1)
print(list2)

print("\n---Question 19---")

import copy

list1 = [10, 20, 30]
list2 = copy.copy(list1)

list2[0] = 100

print(list1)
print(list2)

print("\n---Question 20---")

import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)

print(list1)
print(list2)

print("\n---Question 21---")

import copy

list1 = [1, 2, 3]
list2 = copy.deepcopy(list1)

print(list2)

print("\n---Question 22---")

import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)

print(list1)
print(list2)

print("\n---Question 23---")

import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)

list2[0][0] = 10

print(list1)
print(list2)

print("\n---Question 24---")

import copy

list1 = [[1, 2], [3, 4]]

shallow = copy.copy(list1)
deep = copy.deepcopy(list1)

print("Original:", list1)
print("Shallow copy:", shallow)
print("Deep copy:", deep)

print("\n---Question 25---")

import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)

list2[0][0] = 10

print("Original list:", list1)
print("Copied list:", list2)