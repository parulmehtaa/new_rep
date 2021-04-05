name=input("Enter your name: ")
age=int(input("Enter your age: "))

if (age)>=18:
    print("hello",name,"you are",age,"years old")
    print(f"hello {name} you are eligible for the vote")

print("Thank you!")

"""
$ python 02_class5.py
Enter your name: parul
Enter your age: 18
hello parul you are 18 years old
hello parul you are eligible for the vote
Thank you!
yes, number is even

"""

n=250
if n%2==0:
    print("yes, number is even")
else:
    print("number is odd") 