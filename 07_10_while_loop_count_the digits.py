def count_the_digits(n):
    j=1
    i=0
    while (n//j)>=1:
        i=i+1
        j=j*10
    return i

def main():
    n=int(input("Enter the value of n: "))
    c=count_the_digits(n)
    print(c)

main()
