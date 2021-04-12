def cubes_of_natural_n(n):
    sum=0
    i=1
    while i<=n:
        sum=sum+i**3
        i=i+1
    return sum

def main():
    sum=0
    n=int(input("Enter the value of n:                        "))
    sum=cubes_of_natural_n(n)
    print(f"sum of cubes of first n natural numbers is:  {sum} ")

main()
