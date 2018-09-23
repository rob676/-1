a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
z=a%2
if z==0.5:
    z=z+0/5
a=a/2
x=b%2
if x==0.5:
    x=x+0/5
b=b/2
s=c%2
if s==0.5:
    s=s+0.5
c=c/2
d=a+b+c+z+x+s
print("кількість столів",d)
