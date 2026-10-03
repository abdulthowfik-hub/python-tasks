print("\n---Question 1---")

age=25
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

print("\n---Question 2---")

mark= 85
if mark >= 90:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B")
else:
    print("Grade: C")

print("\n---Question 3---")

num=-5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("\n---Question 4---")

day=3
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid day")

print("\n---Question 5---")

units=int(input("Enter number of units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2.5
elif units <= 500:
    bill = units * 4
else:
    bill = units * 6 

print("\n---Question 6---")

weight=70
height=1.75
bmi = weight / (height ** 2)
print("BMI=",bmi)
if bmi< 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

print("\n---Question 7---")

a=25
b=50
c=75
if a>=b and a>=c:
    print("a is the largest")
elif b>=a and b>=c:
    print("b is the largest")
else:
    print("c is the largest")

print("\n---Question 8---")

amount = float(input("Enter purchase amount: "))

if amount < 1000:
    discount = 0
elif amount < 5000:
    discount = 5
elif amount < 10000:
    discount = 10
else:
    discount = 20

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Discount =", discount, "%")
print("Discount Amount =", discount_amount)
print("Final Amount =", final_amount)

print("\n---Question 9---")

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

print("\n---Question 10---")

balance = 5000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Balance =", balance)

elif choice == 2:
    amount = float(input("Enter deposit amount: "))
    balance = balance + amount
    print("New Balance =", balance)

elif choice == 3:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance = balance - amount
        print("New Balance =", balance)
    else:
        print("Insufficient Balance")

elif choice == 4:
    print("Thank you")

else:
    print("Invalid choice")