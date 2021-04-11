def rhombus(n,num):
    j=0
    while j<=n+num:
        if j>n:
            print("*", end="")
        else:
            print(" ",end="")
        j=j+1
    print()

def main():
    num=int(input("Enter the value of n"))
    i=0
    while i<num:
        rhombus(i,num)
        i=i+1

main()