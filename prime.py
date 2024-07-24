#checking prime number 
import math
def isprime(num):
    divisor_count = 0
    for i in range (1,int(math.sqrt(num))):   
        if (num%i == 0):
            divisor_count+=1
    i+=1
    if (divisor_count == 0 ):      
        print(f"{num} is prime")
    else :
        print(f"{num} is not prime")

num = int(input("Enter a number to check prime or not\n"))
