# Find and display the largest number of a list without using built-in function max(). Your program should
# ask the user to input values in list from keyboard.


# a = [10, 30, 80, 23, 12]

# large= max(a)
# print(large)


b=[]

num=int(input("Enter No of element:"))
for i in range(num):
    ele=int(input(f"Enter Element{i+1}:"))
    b.append(ele)

print("List:", b)
larger=max(b)
print(larger)

