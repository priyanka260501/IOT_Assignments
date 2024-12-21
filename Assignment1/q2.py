#Write a program to accept three integer numbers and find its average.

a=int(input("Enter No:"))
b=a%10
a//=10

c=a%10
a//=10

d=a%10
a//=10

e=a%10
a//=10

print(f"Face value= {e}\t{d}\t{c}\t{b}")
print(f"{a}= {e}000 +{d}00 +{c}0 +{b}")

print(f"reverse:{b}{c}{d}{e}")