#program to print multiplication table of any number 
num = int(input("Enter the multiplicand : "))
limit = int(input("Enter the multiplier :"))
i=1
print("This is the multiplication table for {}".format(num)) #using .format
while (i <= limit):
    result = num*i
    print(f"{num} * {i} = {result}")                        #using f string
    i+=1

age = int(input("enter age "))
print(f"My age is {age}")
print("My age is {}".format(age))