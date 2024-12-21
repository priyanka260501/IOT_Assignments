# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

b=[]

num=int(input("Enter No of element:"))
for i in range(num):
    ele=int(input(f"Enter Element{i+1}:"))
    b.append(ele)

print("List:", b)
