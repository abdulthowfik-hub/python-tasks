numbers=(10,20,30,40,50)
print("Tuples:",numbers)
print("length:",len(numbers))

print("\n--- Concatenation ---")

tuples1=(1,2,3)
tuples2=(4,5,6)
result=tuples1+tuples2
print("Tuple 1:",tuples1)
print("Tuple 2:",tuples2)
print("Concatenated Tuple:",result)

print("\n--- Ascending order ---")

numbers=(50,30,10,40,20)
ascending= tuple(sorted(numbers))
print("Original Tuple:",numbers)
print("Ascending Order:",ascending)

print("\n--- Descending order ---")

numbers=(50,30,10,40,20)
descending= tuple(sorted(numbers,reverse=True))
print("Original Tuple:",numbers)
print("descending Order:",descending)

print("\n--- reverse ---")

numbers=(10,20,30,40,50)
reverse= numbers[::-1]
print("original Tuple:",numbers)
print("reversed Tuple:",reverse)

print("\n--- count ---")

numbers=(10,20,10,30,10,40)
result=numbers.count(10)
print("Tuple:",numbers)
print("Count of 10:",result)

print("\n--- index ---")

numbers=(10,20,30,40,50)
result=numbers.index(30)
print("Tuple:",numbers)
print("Index of 30:",result)

print("\n--- slicing ---")

numbers=(10,20,30,40,50)
result=numbers[1:4]
print("Tuple:", numbers)
print("Sliced Tuple:",result)

print("\n--- add Dictionary ---")

student= {"Name": "Thowfik", "Age": 22}
student["course"]="Data science"
print(student)

print("\n--- pop ---")

student= {"Name": "Thowfik", "Age": 22, "course": "Data science"}
student.pop("Age")
print( student)