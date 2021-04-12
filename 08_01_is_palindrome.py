def reverse(n):
    i=n
    rev=0
    while i>0:
        rem=i%10
        rev=rev*10+rem
        i=i//10
    return rev

def main():
    n=int(input("Enter the value of n: "))
    rev=reverse(n)
    if rev==n:
        print("yes, this is a palindrome")
    else:
        print("no")
    print(rev)

main()
