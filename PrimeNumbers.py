# Write a program to print prime numbers in given range of values
# (lowest range value and upper range value).

# Sample Input: Enter the Lowest Range Value: 1
#               Enter the Upper Range Value: 100
# Sample Output: The Prime Numbers in the range are:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
x = int(input("Enter the Lowest Range Value : "))
y = int(input("Enter the Upper Range Value: "))
print("The Prime Numbers in the range are:")
for i in range(x,y+1):
    if i>1:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
        if flag==0:
            print(i)