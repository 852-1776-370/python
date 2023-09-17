a=int(input("enter the first numbear "))
b=int(input("enter the second numbear "))
rem=a%b
while(rem!=0):
  a=b
  b=rem
  rem=a%b
print(b)
