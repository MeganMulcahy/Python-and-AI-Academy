# The following program will check which grade a student is from based on their age.
age = int(input("Enter your age: ") or 23)
if (age >= 5) and (age < 12):
    print("You must be in elementary school.")
elif (age >= 12) and (age < 15):
    print("You must be in middle school.")
else:
    print("You must be in high school!")

# The following program tests if the given conditions are true or false.

# Relational Operators
print(9 > 7)
print(10 == 10)
print(1210 >= 1220)
print(3214 <= 3124)
print(1111 < 11111)

# Comparison Keywords
print(not 41 > 80)
print(14567 >= 14657 or 1342 <= 1342)
print(14567 >= 14657 and 1342 <= 1342)

#short hand
a = 3
print('A is posative') if a > 0 else (print('A is zero') if a == 0 else print ('A is negative'))