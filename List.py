#Ques1
marks=[75,60,57,87,96,78,88,92,55,70]
highest=max(marks)
print("highest mark:", highest)

print("\n---Question 2---")

salary=[25000,32000,28000,30000,35000]
lowest_salary=min(salary)
highest_salary=max(salary)
print("lowest salary:", lowest_salary)
print("highest salary:", highest_salary)

print("\n---Question 3---")

numbers=[10,20,30,40,50]
total=sum(numbers)
average=total/len(numbers)
print("Sum:", total)
print("Average:", average)

print("\n---Question 4---")

numbers=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for number in numbers:
    if number % 2==0:
        even.append(number)
    else:
        odd.append(number)
print("Even numbers:", even)
print("Odd numbers:", odd)


print("\n---Question 5---")

numbers=[10,20,30,40,50,60,70,80,90,100]
unique_numbers=[]
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("Original list:", numbers)
print("Without duplicates:", unique_numbers)

print("\n---Question 6---")

numbers=[8,15,25,34,50]
largest=float('-inf')
second_largest=float('-inf')
for number in numbers:
    if number > largest:
        second_largest=largest
        largest=number
    elif number > second_largest and number != largest:
        second_largest=number
print("Second largest number:",second_largest)

print("\n---Question 7---")

numbers=[10,20,30,40,50]
reversed_list=[]
for number in numbers:
    reversed_list.insert(0,numbers)
print("original list:", numbers)
print("Reversed list:", reversed_list)

print("\n---Question 8---")

list1=[10,20,30,40,50]
list2=[30,40,50,60,70]
common=[]
for number in list1:
    if number in list2:
        common.append(number)
print("Common elements:", common)

print("\n---Question 9---")

cart=[]
while True:
    print("\n1.add product")
    print("2.remove product")
    print("3.view products")
    print("4.exit")
    choice=input("Enter your choice:")
    if choice=="1":
        product=input("Enter product name:")
        cart.append(product)
        print(product,"added.")
    elif choice=="2":
        product=input("Enter product name to remove:")
        if product in cart:
            cart.remove(product)
            print(product,"removed.")
        else:
            print(product,"not found in cart.")
    elif choice=="3":
        print("Shopping cart:",cart)
    elif choice=="4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")

print("\n---Question 10---")

items=["apple","banana","apple","orange","banana"]
items=input("Enter the item to count:")
count=items.count(items)
print(items,"occurs",count,"times")
