a=2003
b=3000
for i in range (a,b):
    if(i%4==0 and(i%100==0 or i%400==0)):
        print(i%100)
        break
    
