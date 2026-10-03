print("\n---Question 1---")

students = {
    "Arun": 85,
    "Rahul": 92,
    "Karthik": 78,
    "Vijay": 95,
    "Sanjay": 88
}
highest_student = max(students, key=students.get)
print("Student with highest mark:", highest_student)
print("Highest mark:", students[highest_student])


print("\n---Question 2---")

employees = {
    "Arun": {"salary": 28000, "department": "HR"},
    "Rahul": {"salary": 35000, "department": "IT"},
    "Karthik": {"salary": 42000, "department": "Finance"},
    "Vijay": {"salary": 25000, "department": "Sales"}
}
print("Employees earning above ₹30,000:")
for name, details in employees.items():
    if details["salary"] > 30000:
        print(name, "-", details["salary"], "-", details["department"])


print("\n---Question 3---")

text = "hello"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequency:", frequency)


print("\n---Question 4---")

sentence = "python is easy and python is powerful"
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequency:", frequency)


print("\n---Question 5---")

products = {
    "Laptop": 55000,
    "Mobile": 25000,
    "Headphones": 3000,
    "Keyboard": 1500
}
product = input("Enter product name: ")
if product in products:
    print("Price:", products[product])
else:
    print("Product not found")


print("\n---Question 6---")

squares = {}
for number in range(1, 11):
    squares[number] = number ** 2
print("Numbers and their squares:")
print(squares)


print("\n---Question 7---")

dict1 = {
    "Name": "Abdul",
    "Age": 21
}
dict2 = {
    "City": "Chennai",
    "Course": "AI and Data Science"
}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)


print("\n---Question 8---")

students = {
    "Arun": 85,
    "Rahul": 32,
    "Karthik": 75,
    "Vijay": 28,
    "Sanjay": 60
}
pass_students = {}
fail_students = {}
for name, mark in students.items():
    if mark >= 40:
        pass_students[name] = mark
    else:
        fail_students[name] = mark
print("Pass Students:", pass_students)
print("Fail Students:", fail_students)


print("\n---Question 9---")

phone_book = {}
while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phone_book[name] = phone
        print("Contact added successfully")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phone_book:
            print("Phone number:", phone_book[name])
        else:
            print("Contact not found")
    elif choice == "3":
        name = input("Enter name to update: ")
        if name in phone_book:
            phone = input("Enter new phone number: ")
            phone_book[name] = phone
            print("Contact updated successfully")
        else:
            print("Contact not found")
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")
    elif choice == "5":
        print("Program ended")
        break
    else:
        print("Invalid choice")

print("\n---Question 10---")

shopping_cart = {
    "Apple": 5,
    "Milk": 2,
    "Bread": 3,
    "Eggs": 10
}
total_quantity = 0
for product, quantity in shopping_cart.items():
    print(product, ":", quantity)
    total_quantity += quantity
print("Total quantity:", total_quantity)