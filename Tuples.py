# Write a program to print list of tuples which has a number and its cube value.
n = int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)
new_lst = [(i,i**3) for i in lst]
print(new_lst)