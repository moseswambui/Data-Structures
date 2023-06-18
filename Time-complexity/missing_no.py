import time
def find_missing_number(numbers):
    n = len(numbers) + 1
    xor_sum = 0

    #XOR all the numbers from 1 to n

    for i in range(1, n + 1):
        xor_sum ^= i

    #XOR all the numbers in the list
    for num in numbers:
        xor_sum ^= num


    return xor_sum

numbers = [1,5,2,7,8,6,4]
start_time = time.time()
missing_number =  find_missing_number(numbers)
end_time = time.time()

execution_time = end_time - start_time
print("missing Number: ", missing_number)
print("Execution time:", execution_time, "seconds")

"""
XOR (exclusive OR) sum is a binary operation that combines two binary values, bit by bit, and produces a result where each bit is set if and only if the corresponding bits in the two values are different.
The XOR operation returns 0 if the bits are the same and 1 if they are different.

In the context of finding a missing number, XOR sum is used to efficiently determine the missing element. By XORing all the numbers in a sequence (e.g., from 1 to n) and XORing the numbers in the given list,
the XOR sum of these two operations will yield the missing number.

Here's an example to illustrate XOR sum:

Let's consider two binary numbers: 1010 and 1101.
   1 0 1 0    (1010)
 ^ 1 1 0 1    (1101)
 ---------
   0 1 1 1    (0111)

As you can see, the XOR operation compares each bit in the two numbers and returns 1 only if the bits are different.
In this case, the XOR sum of 1010 and 1101 is 0111.

XOR sum has some useful properties, such as being commutative (the order of operands does not matter) and self-inverse (XORing the result with one of the operands gives the other operand). These properties make it handy for various bitwise operations and algorithms, including finding missing numbers.
"""

def find_missing_number(numbers):
    xor_sum = 0

    # XOR all the numbers in the list
    for num in numbers:
        xor_sum ^= num

    # XOR all the numbers from the minimum to the maximum in the list
    for i in range(min(numbers), max(numbers) + 1):
        xor_sum ^= i

    return xor_sum

# Example usage
numbers = [40, 41, 45, 42, 47, 48, 46,44]
start_time = time.time()
missing_number =  find_missing_number(numbers)
end_time = time.time()

execution_time = end_time - start_time
print("missing Number: ", missing_number)
print("Execution time:", execution_time, "seconds")


def solution(A):
    actual_sum = 0
    for number in A:
        actual_sum += number

    max_number = len(A) + 1
    #Using Triangula numbers
    expected_sum = (max_number * (max_number + 1) // 2)
    return expected_sum - actual_sum

start_time = time.time()
print(solution([2,3,1,5]))
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
print(solution([1,2,3,4,5,6,7,8,9]))
print(solution([]))