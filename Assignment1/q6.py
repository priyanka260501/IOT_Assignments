
def fac(a):
    if a == 1 or a == 0:
        return 1
    else:
        return (a *fac(a-1))

num=int(input("Enter No:"))
res=fac(num)
print(f"Factorial={res}")
