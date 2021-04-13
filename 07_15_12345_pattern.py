def pattern(n):
    j=0
    while j<=n:
        print(j+1, end="")
        j=j+1
    print()

def main():
    num=int(input("Enter the value of n"))
    i=0
    while i<num:
        pattern(i)
        i=i+1

main()