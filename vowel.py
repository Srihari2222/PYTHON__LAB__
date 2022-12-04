# Write a python program to check the given alphabet is vowel or consonant.

# Sample Input1: Input a letter of the alphabet: d
# Sample Output1: d is a consonant.

# Sample Input2: Input a letter of the alphabet: u
# Sample Output2: u is a vowel.
alpha = input("Input a letter of the alphabet:")
if alpha in "AEIOUaeiou":
    print(alpha + " is a vowel")
else:
    print(alpha + " is a consonant")