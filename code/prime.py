flag=False
n=int(input("enter the no"))
for i in range(2,n/2):
    if(num%i==0):
        flag=True
        break
if flag:
    print("the num is not a prime")
else:
    print("its a prime no.")
