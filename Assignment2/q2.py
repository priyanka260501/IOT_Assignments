#write a function to return compound interest
#C.I.=(p((1+(r/100))^t)-p)


def fun(p,r,t):

    ci=(p((1+(r/100)),t)-p)
    print(f"CI={ci}")
    return ci
a=int(input("Enter Principal:"))
b=int(input("Enter Rate of instrest:"))
c=int(input("Enter Time:"))

res=fun(a,b,c)
print(f"CI={res}")