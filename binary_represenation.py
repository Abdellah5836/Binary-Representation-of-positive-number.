'''
We want
to print the binary representation of a positive number. In order to do so,
we can use a simple algorithm that divides by '2' until we reach '0' and
collects the remainders. When we reverse the list of remainders we
collected, we get the binary representation of the number we started with:
6 / 2 = 3 (remainder: 0)
3 / 2 = 1 (remainder: 1)
1 / 2 = 0 (remainder: 1)
List of remainders: 0, 1, 1.
Reversed is 1, 1, 0, which is also the binary representation of 6.
'''

from sympy import rem


remainders_dict = []
result_list = []
def Binary_num(remainders_dict, result_list):
    """
    Baniary representation of a positive number
    """
    query = input("Enter a Positive Number: ")
    if int(query) < 0:
        print("**Please, Enter a POSITIVE Number.**")
        return 0
    pos_num = int(query)
    while pos_num > 0:
        result_list.append(pos_num)
        remainder = pos_num % 2
        remainders_dict.append(remainder)
        pos_num //= 2



def display_binay_num(remainders_dict, result_list):
    """
    Display remainders list content
    """
    print(f"List of remainders: {remainders_dict}")
    print("~~" * 20)
    print(f"Reversed is {remainders_dict[::-1]},"
        f" which is also the binary representation of {result_list[0]}.")



print("~~" * 20)
Binary_num(remainders_dict, result_list)
print("~~" * 20)
print(f"Numberes Calculated:\n\t{result_list}")
print("~~" * 20)
display_binay_num(remainders_dict, result_list)
