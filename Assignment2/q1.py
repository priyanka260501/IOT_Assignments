
#Write a function to return simple interest
#S.I. = (P × R × T)/100

def fun(p,r,t):
    si=(p*r*t)/100
    print(f"SI={si}")
    return si
a=int(input("Enter Principal:"))
b=int(input("Enter Rate of instrest:"))
c=int(input("Enter Time:"))

res=fun(a,b,c)
print(f"SI={res}")
