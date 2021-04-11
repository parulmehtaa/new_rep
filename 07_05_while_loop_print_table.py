def table_print(n):
    i=1
    while i <=10:
        print("{}*{}={}".format(n,i,n*i))
        i=i+1

def main():
    n=int(input("Enter the value of n: "))
    table_print(n)
main()
