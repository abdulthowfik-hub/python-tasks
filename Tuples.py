students = ("Arun","Bala","Charan","David","Kumar")
for name in students:
    print(name)

print("\n---Question 2---")

numbers = (10, 20, 30, 40, 50)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

print("\n---Question 3---")

numbers = (10, 20, 10, 30, 10, 40)
value = 10
print("Count:", numbers.count(value))

print("\n---Question 4---")

numbers = (10, 20, 30, 40, 50)
value = 30
print("Index:", numbers.index(value))

print("\n---Question 5---")

numbers = (10, 20, 30)
numbers_list = list(numbers)
numbers_list.append(40)
numbers_list.append(50)
numbers = tuple(numbers_list)
print(numbers)

print("\n---Question 6---")

student = ("Arun", 20, 85)
name, age, mark = student
print("Name:", name)
print("Age:", age)
print("Mark:", mark)

print("\n---Question 7---")

marks = (75, 85, 90, 60, 95, 70)
count = 0
for mark in marks:
    if mark > 80:
        count += 1
print("Students above 80:", count)

print("\n---Question 8---")

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
result = tuple1 + tuple2
print(result)

print("\n---Question 9---")

fruits = ("Apple", "Banana", "Mango", "Orange")
item = "Mango"
if item in fruits:
    print("Item exists in the tuple")
else:
    print("Item does not exist in the tuple")

print("\n---Question 10---")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 10)

even_numbers = ()

for number in numbers:
    if number % 2 == 0:
        even_numbers += (number,)

print(even_numbers)