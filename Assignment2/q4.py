#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
b=[]

num=int(input("Enter No of element:"))
for i in range(num):
    ele=input(f"Enter Element{i+1}:")
    b.append(ele)

print("List:", b)
larger=max(b)
print(larger)