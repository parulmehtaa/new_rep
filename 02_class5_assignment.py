a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if a<b:
    print(f"Minimum is: {a}")
else:
    print(f"Minimum is: {b}")

"""
$ python 02_class5_assignment.py
Enter 1st number: 12
Enter 2nd number: 11
Minimum is: 11

$ python 02_class5_assignment.py
Enter 1st number: 12
Enter 2nd number: 11
Minimum is: 11


"""

if a>b:
    if a>c:
        print(f"max is {a}")
if b>c:
    if b>a:
        print(f"max is {b}")

if c>a:
    if c>b:
        print(f"max is {c}")

"""
$ python 02_class5_assignment.py
Enter 1st number: 12
Enter 2nd number: 14
Enter 3rd number: 11
Minimum is: 12
max is 14
"""