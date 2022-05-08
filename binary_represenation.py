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


from text_colors import TextColors

tc = TextColors

def binary_rep():
    list_remainders = []

    query = input(f"{tc.magenta}[+]Enter a positive number:{tc.reset} ")
    num = int(query)
    if num < 0:
        return f"{tc.red}[!]Unrecognized number!\n{tc.reset}"

    while num > 0:
        binary = num % 2
        list_remainders.append(binary)
        num //= 2
        
    print(f"\n{tc.green}[~]List of remainders:{tc.reset} {list_remainders}")
    list_remainders.reverse()
    print(f"\n{tc.green}[~]Reserved is:{tc.reset} {list_remainders}")

    int_num = len(list_remainders)
    list_binary = [ 2 ** item for item in range(int_num) ]
    list_binary.reverse()
    #print(list_binary)

    product = [list_remainders[i] * list_binary[i] for i in range(len(list_remainders))]
    #print(product)
    result = sum(product)
    #print(f"\n{tc.cyan}Which is also the binary representation of{tc.blue} {result}.{tc.reset}")
    return f"\n{tc.cyan}[√]Which is also the binary representation of{tc.blue} {result}.{tc.reset}"


