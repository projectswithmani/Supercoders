# Write a python function, check_double (number) which accepts a whole number and returns True if it satisfies the given conditions.

# 1. The number and its double should have exactly the same number of digits. 2. Both the numbers should have the same digits, but in different order.

# Otherwise it should return False.

# Example: If the number is 125874 and its double, 251748, 1 contain exactly the same digits, but in a different order.  i.isdigit
def check_double_number(number):
    num_str = str(number)
    double = str(number*2)

    if len(num_str) != len(double):
        return False
    for i in num_str:
        if i not in double:
            return False
    for i in num_str:
        if num_str.count(i) != double.count(i):
            return False
    return True
print(check_double("anyvalue"))

































































































