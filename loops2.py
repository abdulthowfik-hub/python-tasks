print("\n---Question 1---")

for i in range (1,21):
    if i==10:
        continue
    print(i,end="")

print("\n---Question 2---")

numbers=[10,20,30,40,50]
for i in numbers:
    if i ==30:
        pass
    print(i, end="")

print("\n---Question 3---")

for i in range(1,11):
    if i%2==0:
        continue
    print(i,end="")

print("\n---Question 4---")

num=[5,8,12,15,20,25]
for i in num:
    if i>15:
        break
    print(i,end="")

print("\n---Question 5---")

names=["Arun","Bala","Cathy","Divya","Esha"]
for name in names:
    if name=="Cathy":
        continue
    if name=="Divya":
        pass
    print(name)