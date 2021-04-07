def cubes_of_natural_n(n):
    sum=0
    for i in range(1,n+1,1):
        sum=sum+i**3
    return sum

def main():
    sum=0
    n=int(input("Enter the value of n:                        "))
    sum=cubes_of_natural_n(n)
    print(f"sum of cubes of first n natural numbers is:  {sum} ")

main()
