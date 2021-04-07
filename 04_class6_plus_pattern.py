
def print_plus_pattern(n):
    for j in range(n):
        print("+",end=" ")
    print("\n")

def print_space_pattern(n):
    s=0
    for j in range(n):
        if j==((n-1)/2) or j== n/2:
            print("+", end=" ")
            #print(s)
            #s=s+1
        else:
            print(" ",end=" ")
            #print(s)
            #s=s+1
    print("\n")


def main():
    num=int(input("Enter the value of n: "))
    for i in range(2*num):
        if i==(num-1):
            print_plus_pattern(num)
        else:
            print_space_pattern(num)



main()
            


    