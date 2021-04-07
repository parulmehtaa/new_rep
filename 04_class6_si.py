def simple_interest(p,n,r):
    si=(p*n*r)/100
    return si

def main():
    si=0
    p=int(input("Enter the value of Principal:             "))
    r=int(input("Enter the rate of interest in percentage: "))
    n=int(input("Enter the number of yeras:                "))
    si=simple_interest(p,n,r)
    print(f"simple interest of {p}, {n}, {r} is:       {si} ")

main()
