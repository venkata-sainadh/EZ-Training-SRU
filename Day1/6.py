#Magical Prime
import math as m
def isprime(num):
    if num==2 or num==3:
        return 1
    if num%2==0 or num%3==0:
        return 0
    for i in range(5,int(m.sqrt(num)),6):
        if(num%i==0):
            return 0
    return 1
def magicalPrime(st,en):
    for i in range(st,en+1):
        rev=str(i)
        rev=rev[::-1]
        rev=int(rev)
        if(isprime(i)==1 and isprime(rev)==1):
            print(i,end=" ")
start=int(input("Start of range:"))
end=int(input("End of range:"))
magicalPrime(start,end)
