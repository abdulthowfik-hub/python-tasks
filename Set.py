print("\n---Question 1---")

numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = set(numbers)
print(unique_numbers)

print("\n---Question 2---")

set_a = {"Arun", "Bala", "Kumar", "David"}
set_b = {"Kumar", "David", "Ravi", "John"}
common = set_a.intersection(set_b)
print(common)

print("\n---Question 3---")

set_a = {"Arun", "Bala", "Kumar", "David"}
set_b = {"Kumar", "David", "Ravi"}
result = set_a.difference(set_b)
print(result)

print("\n---Question 4---")

class_a = {"Arun", "Bala", "Kumar"}
class_b = {"Kumar", "David", "Ravi"}
unique_students = class_a.union(class_b)
print(unique_students)

print("\n---Question 5---")

set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}
if set_b.issubset(set_a):
    print("Set B is a subset of Set A")
else:
    print("Set B is not a subset of Set A")

print("\n---Question 6---")

set_a = {1, 2, 3}
set_b = {4, 5, 6}
if set_a.isdisjoint(set_b):
    print("The sets are disjoint")
else:
    print("The sets are not disjoint")

print("\n---Question 7---")

numbers = set(range(1, 21))
for number in range(2, 21, 2):
    numbers.remove(number)
print(numbers)

print("\n---Question 8---")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))

print("\n---Question 9---")

department_a = {"Arun", "Bala", "Kumar", "David"}
department_b = {"Kumar", "David", "Ravi", "John"}
both_departments = department_a.intersection(department_b)
print(both_departments)
print("\n---Question 10---")

purchased_ids = {101, 102, 103, 104, 105}
product_id = 103
if product_id in purchased_ids:
    print("Product was purchased")
else:
    print("Product was not purchased")