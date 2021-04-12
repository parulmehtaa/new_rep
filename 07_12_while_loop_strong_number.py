def fact(num):
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i=i+1
    return fact

def is_strong(n):
    i=n
    rem=0
    sum=0
    fac=0
    while i>0:
        rem=i%10
        fac=fact(rem)
        sum=sum+fac
        i=i//10
    if sum==n:
        return 1
    else:
        return 0

def main():
    num=int(input("Enter the value of n"))
    
    if is_strong(num):
        print("yes")
    else:
        print("no")

main()