print("\n---Question 1---")

num=10
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("zero")

print("\n---Question 2---")

num=5
if num%2==0:
    print("Even")
else:
    print("Odd")

print("\n---Question 3---")

age=16
if age >18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print("\n---Question 4---")

mark=70
if mark>=35:
    print("pass")
else:
    print("fail")

print("\n---Question 5---")

num=35
if num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

print("\n---Question 6---")

a=25
b=15
if a>b:
    print("Greater number:",a)
else:
    print("Greater number:",b)

print("\n---Question 7---")

a=10
b=20
c=30
if a>=b and a>=c:
    print("Largest:",a)
elif b>=a and b>=c:
    print("Largest:",b)
else:
    print("Largest:",c)

print("\n---Question 8---")

age=22
if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior Citizen")

print("\n---Question 9---")

num=50
if num%3==0 and num%5==0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

print("\n---Question 10---")

temp=25
if temp<20:
    print("Cold")
elif temp<=30:
    print("Normal")
else:
    print("Hot")    

print("\n---Question 11---")

mark=85
if mark>=90:
    print("Grade: A")
elif mark>=75:
    print("Grade: B")
elif mark>=50:
    print("Grade: C")
elif mark<=35:
    print("Grade: D")
else:
    print("Fail")

print("\n---Question 12---")

num=55
if 10<= num <= 99:
    print("Two-digit number")
else:
    print("Not a two-digit number")

print("\n---Question 13---")

character = input("Enter a character: ")

if character in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
 
print("\n---Question 14---")

height=135
if height>120:
    print("Eligible for ride")
else:
    print("Not eligible for ride")

print("\n---Question 15---")

num=20
if num>0 and num %2==0:
    print("Positive and even")
else:
    print("Not positive and even")

print("\n---Question 16---")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

print("\n---Question 17---")

mark1 = 60
mark2 = 70
mark3 = 80

average = (mark1 + mark2 + mark3) / 3

print("Average:", average)

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Pass")
else:
    print("Fail")

print("\n---Question 18---")

year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

print("\n---Question 19---")

a = 5
b = 5
c = 5

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

print("\n---Question 20---")

num = 12

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Divisible by neither")

print("\n---Question 21---")

age = 25

if age < 5:
    print("Free")
elif age <= 12:
    print("Ticket Price: ₹50")
elif age <= 59:
    print("Ticket Price: ₹100")
else:
    print("Ticket Price: ₹70")

print("\n---Question 22---")

username = "admin"
password = "1234"

if username != "admin":
    print("Invalid Username")
elif password != "1234":
    print("Incorrect Password")
else:
    print("Login Successful")

print("\n---Question 23---")

units =250

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
elif units <= 300:
    bill = units * 5
else:
    bill = units * 7

print("Electricity Bill: ₹", bill)

print("\n---Question 24---")

mark = 82

if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
elif mark >= 50:
    grade = "C"
elif mark >= 35:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)

if mark >= 35:
    print("Status: Pass")
else:
    print("Status: Fail")

print("\n---Question 25---")

amount = 6000

if amount < 1000:
    discount = 0
elif amount < 5000:
    discount = 10
elif amount < 10000:
    discount = 20
else:
    discount = 30

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Discount:", discount, "%")
print("Final Amount: ₹", final_amount)

print("\n---Question 26---")

salary = 400000

if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.10
else:
    tax = salary * 0.20

print("Tax Amount: ₹", tax)

print("\n---Question 27---")

speed = 75

if speed < 40:
    print("Slow")
elif speed <= 60:
    print("Normal")
elif speed <= 80:
    print("Fast")
else:
    print("Over Speed")

print("\n---Question 28---")

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")

print("\n---Question 29---")

month = 4

if month == 2:
    print("28 or 29 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month >= 1 and month <= 12:
    print("31 days")
else:
    print("Invalid Month")

print("\n---Question 30---")

age = int(input("Enter your age: "))
tickets = int(input("Enter number of tickets: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 100
elif age <= 59:
    price = 200
else:
    price = 150

total = price * tickets

if tickets > 5:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Ticket Price: ₹", price)
print("Total Amount: ₹", total)
print("Discount: ₹", discount)
print("Final Bill: ₹", final_bill)