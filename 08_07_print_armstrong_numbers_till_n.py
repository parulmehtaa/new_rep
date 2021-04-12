def count_the_digits(n):
    j=1
    i=0
    while (n//j)>=1:
        i=i+1
        j=j*10
    return i

def power_num(n,num_digits):
    sum=0
    sum=n**num_digits
    return sum


def is_strong(n):
    i=n
    rem=0
    sum=0
    fac=0

    num_digits=count_the_digits(n)
    while i>0:
        rem=i%10
        fac=power_num(rem,num_digits)
        sum=sum+fac
        i=i//10
    if sum==n:
        
        return 1
    else:
        
        return 0

def main():
    n=int(input("Enter the value of n"))
    
    for num in range(1,n+1,1):
        if is_strong(num):
            print(num)
        

main()