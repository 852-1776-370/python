decimal=int(input("enter the decimal number"))
c=decimal
b=[]
for i in range(0,c,1):
      c=c//2
      d=c%2
      b.append(d)
i=i-1
while(i>=0):
    print(b)
    i=i-1
