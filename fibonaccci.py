#program to print n fibonacci numbers
num = int(input("Enter a number : "))
prev , cur = 0, 1
next = 0
if num<0 :
    print("Invalid Input")

for i in range (0, num):
    print(next)
    prev=cur
    cur=next
    next = prev + cur


#print upto nth fibonacci number

num = int(input("Enter a number : "))
prev , cur = 0, 1
next = 0
if num<0 :
    print("Invalid Input")

for i in range (0, num):
    print(next)
    prev=cur
    cur=next
    next = prev + cur
    if next == num:
        print(next)
        break
