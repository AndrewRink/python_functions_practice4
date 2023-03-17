# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(int1, int2, int3):
    print (max(int1, int2, int3))

max_num(7,2,3)


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(myList):
    if len(myList) == 0:
        return 0
    prod = myList[0]

    if len(myList) >1:
        for i in myList[1:]:
            prod = prod * i

    return prod

print (mult_list([1,2,3]))


# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]

reverseText = rev_string("reverse")
print(reverseText)

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(x, num1, num2):
    return x in range(num1, num2)

print(num_within(4, 2, 6))
print(num_within(7, 3, 6))



# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    for i in range(1, n+1):
        for n in range(0, n-i+1):
            print('', end='')

        C=1
        for n in range(1, i+1):
            print('', C, sep='', end='')

            C = C * (i -n) // n
        print()

pascal(5)