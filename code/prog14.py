
#prog 14
a=int(input("enter no.1"))
b=int(input("enter no.2"))
c=int(input("enter no.3"))
d=int(input("enter no.4"))
if(a%2==0):
    print("the value of a is even")
if(b%2==0):
    print("the value of b is even")
if(c%2==0):
    print("the value of c is even")
if(d%2==0):
    print("the value of d is even")

#prog 13

setpassword1=int(input("enter the password 1"))
setpassword2=int(input("enter the password 2"))

password1=int(input("enter ur 1st passsword to login"))

if(setpassword1==password1):
    password2=int(input("enter ur 2nd passsword to login"))
    if(setpassword2==password2):
        print("welcome to ur account")
    else:
        print("2nd password is wrong")
else:
    print("1st password is wrong")


#prog 15
n=int(input("enter the value of n"))
a=n
d1=a%10
print(d1)
a=int(a/10)
d2=a%10
print(d2)
a=int(a/10)
d3=a%10
print(d3)


#prog 16

n1=int(input("enter the value of n"))
a=n1
d2=a%10
print(d2)

n2=int(input("enter the value of n"))
a=n2
d4=a%10
print(d4)
if(d2>d4):
    print(f"the value of last digit of {n1} is greater than {n2}")
else:
     print(f"the value of last digit of {n2} is greater than {n1}")


