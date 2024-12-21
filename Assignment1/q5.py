# The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F



a=int(input("Enter sub1 :"))
b=int(input("Enter sub2 :"))
c=int(input("Enter sub3 :"))
cal=(a+b+c)/3

max=0
if cal>=90 and cal<100 :
    print(f"Average Grade= A")
    max=cal
elif cal>=80 and cal<89:
    print(f"Average Grade= B")
    max=cal
elif cal>=70 and cal<79:
    print(f"Average Grade= C")
    max=cal
elif cal>=60 and cal<69 :
    print(f"Average Grade= D")
    max=cal
else :
    print(f"Average Grade= F")
    max=cal
print(f"Average:{max}")