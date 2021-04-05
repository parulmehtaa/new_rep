a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
d=int(input("Enter 4th number: "))

# minimum of two numbers
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

# max of 4 numbers
if a>b:
    if a>c:
        if a>d:
            print(f"max is {a}")
if b>c:
    if b>a:
        if b>d:
            print(f"max is {b}")

if c>a:
    if c>b:
        if c>d:
            print(f"max is {c}")

if d>a:
    if d>b:
        if d>c:
            print(f"max is {d}")


"""
$ python 02_class5_assignment.py
Enter 1st number: 12
Enter 2nd number: 14
Enter 3rd number: 11
Minimum is: 12
max is 14
"""

# min of 3 numbers
if a<b:
    if a<c:
        print(f"min is {a}")
if b<c:
    if b<a:
            print(f"min is {b}")

if c<a:
    if c<b:
        print(f"min is {c}")

# min of 4 numbers
if a<b:
    if a<c:
        if a<d:
            print(f"min is {a}")
if b<c:
    if b<a:
        if b<d:
            print(f"min is {b}")

if c<a:
    if c<b:
        if c<d:
            print(f"min is {c}")

if d<a:
    if d<b:
        if d<c:
            print(f"min is {d}")

# min of 3 numbers using logical operators

if a<b and a<c:
    print(f"min is {a}")
elif b<c:
    print(f"min is {b}")
else:
    print(f"min is {c}")

"""
$ python 02_class5_assignment.py
Enter 1st number: 12
Enter 2nd number: 15
Enter 3rd number: 18
Enter 4th number: 09
Minimum is: 12
max is 18
min is 12
min is 9
min is 12
"""