def cyclic_rotation(arr, k):
    n = len(arr)
    rotated_arr = [0] * n

    for i in range(n):
        rotated_index = (i + k) % n
        rotated_arr[rotated_index] = arr[i]

    return rotated_arr

# Example usage
numbers = [1, 2, 3, 4, 5]
k = 5

rotated_numbers = cyclic_rotation(numbers, k)
print("Original array:", numbers)
print("Rotated array:", rotated_numbers)
"""
In this code, the cyclic_rotation function takes an array arr and the number of positions to rotate k as input. It creates a new array rotated_arr with the same length as arr.

For each element in arr, it calculates the rotated index by adding k to the current index and taking the modulus (%) of n, where n is the length of arr. The modulus operation ensures that the index wraps around to the beginning of the array when it exceeds the length.

The element at the current index of arr is then assigned to the corresponding rotated index in rotated_arr.

Finally, the function returns the rotated_arr.

In the example usage, the numbers array is rotated by 3 positions to the right. The original array and the rotated array are printed for comparison.

Note that the above code assumes that k is a positive integer and not greater than the length of the array. Adjustments may be required if you need to handle other scenarios, such as negative k or k greater than the array length
"""

#CODILITY

def solution(A, k):
    result = [None] * len(A)

    for i in range(len(A)):
        result [(i + k )% len(A)] = A[i]

    return result

print(solution([1,2,3,4,5], 5))