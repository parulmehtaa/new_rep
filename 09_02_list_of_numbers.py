import sys
numbers=[0,1,2,3,4,10,9,7]
max=-sys.maxsize
min=sys.maxsize
sum=0
product=1
for item in numbers:
    sum=sum+item
    product=product*item

    if item>max:
        max=item
    if item<min:
        min=item

print(f"sum of {numbers} is: {sum}")
print(f"product of {numbers} is: {product}")
print(f"max of {numbers} is: {max}")
print(f"min of {numbers} is: {min}")
