
def print_plus_pattern(n):
    j=0
    while j<n:
        print("+",end=" ")
        j=j+1
    print("")

def print_space_pattern(n):
    s=0
    j=0
    while j<n:
        if j==((n-1)/2) or j== n/2:
            print("+", end=" ")
            #print(s)
            #s=s+1
        else:
            print(" ",end=" ")
            #print(s)
            #s=s+1
        j=j+1
    print("")


def main():
    num=int(input("Enter the value of n: "))
    i=0
    while i< (2*num):
        if i==(num-1):
            print_plus_pattern(num)
        else:
            print_space_pattern(num)
        i=i+1


main()
            


    