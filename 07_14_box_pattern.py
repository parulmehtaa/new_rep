
def print_plus_pattern(n):
    for j in range(n):
       print("+",end=" ")
    print()

def print_space_pattern(n):
    s=0
    for j in range(n):
        if (j==0 or j==n-1):
            print("+", end=" ")
            #print(s)
            #s=s+1
        else:
            print(" ",end=" ")
            #print(s)
            #s=s+1
    print()


def main():
    num=int(input("Enter the value of n: "))
    for i in range(num):
        if (i==0 or i==num-1):
            print_plus_pattern(num)
        else:
            print_space_pattern(num)



main()
            


    