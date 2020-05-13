numbers=[]
positives =[]
length = int(input("Enter the size of list : "))
print("Enter the elements : ")

for i in range(length):
    numbers.append(int(input()))

for i in range(length):
    if numbers[i]>=0:
        positives.append(numbers[i])

print(f"Original List : {numbers} ")
print(f"Numbers that are positive : {positives}")
