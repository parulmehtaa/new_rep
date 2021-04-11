def fact(num):
    fact=1
    i=num
    while i>=1:
        fact=fact*i
        i=i-1
    return fact

def main():
    num=int(input("Enter the value of n"))
    print("Factorial of {} is: {}".format(num, int(fact(num))))

main()