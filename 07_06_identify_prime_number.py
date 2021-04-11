def prime(n):
    i=2
    s=1
    while i <n:
        if n%i==0:
            s=0
        i=i+1
    return s
def main():
    n=int(input("Enter the value of n: "))
    s=prime(n)
    if (s):
        print("yes")
    else:
        print("no")
main()
