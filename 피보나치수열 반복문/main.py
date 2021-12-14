count=1
n1=1
n2=1
temp=0
print(n1)
print(n2)

while count<49:
    temp=n1
    n1=n2
    n2=temp+n2 
    print(n2)
    count += 1