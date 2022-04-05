# Binary-Representation-of-positive-number.
What if we want to print the binary representation of a positive number. In order to do so, we can use a simple algorithm that divides by 2 until we reach 0 and collects the remainders. When we reverse the list of remainders we collected, we get the binary representation of the Number we started with.
take as an example:
# 6 / 2 = 3 (remainder: 0)
# 3 / 2 = 1 (remainder: 1)
# 1 / 2 = 0 (remainder: 1)
# List of remainders: 0, 1, 1
# reversed is 1, 1, 0, which is also the binary representation of 6.
