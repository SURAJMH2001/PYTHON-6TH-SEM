a=0
c=0
sum=0
for i in range (10):
    c=c+1
    a=int(input("enter the number"))
    sum=sum+a
    if a==100 or a==0:
        c=c-1
        break
print(sum/c)
