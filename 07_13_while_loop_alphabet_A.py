
def print_line_pattern(n):
    j=0
    while j<n:
        print("+",end=" ")
        j=j+1
    print("")

def print_space_pattern(n):
    
    j=0
    while j<n:
        if j==0 or j== n-1:
            print("+", end=" ")
            
        else:
            print(" ",end=" ")
            
        j=j+1
    print("")


def main():
    num=int(input("Enter the value of n: "))
    i=0
    while i< (num):
        if i==(num-1)//2 or i==0:
            print_line_pattern(num)
        else:
            print_space_pattern(num)
        i=i+1


main()
            


    