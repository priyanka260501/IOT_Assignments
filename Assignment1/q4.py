#Write a Python function to find the maximum of three numbers.

no1=int(input("Enetr Num1 :"))
no2=int(input("Enetr Num2 :"))
no3=int(input("Enetr Num3 :"))

max=0
if no1 >no2 and no1>no3   :
    print("Num1 is greater")
    max=no1
elif no2 > no3 and no2>no1 :
    print("Num2 is greater")
    max=no2
else :
    print("Num3 is greater")
    max=no3
print(f"Max Value:{max}")