def Print(n):
    if (n%10==0): # this is lhe terminating base case
        return Print(n*10)
    else:
        print (n)
        return Print(n+1) 
print(Print(4))
