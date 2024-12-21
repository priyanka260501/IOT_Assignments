
# Write a Python Program find an area of a rectangle and perimeter of the rectangle.
def fun(l,w):
    peri=2*(l+w)
    print(f"Perimeter={peri}")
    return l*w
a=int(input("Enter length:"))
b=int(input("Enter width:"))
res=fun(a,b)
print(f"Area={res}")

