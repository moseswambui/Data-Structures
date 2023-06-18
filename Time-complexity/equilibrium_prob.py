def find_pivot(numbers):
    total_sum = sum(numbers)
    left_sum = 0

    for i, num in enumerate(numbers):
        total_sum -= num

        if left_sum == total_sum:
            return i

        left_sum += num

    # If no pivot is found, return -1
    return -1

# Example usage
numbers = [3,1,2,4,3]
pivot = find_pivot(numbers)
if pivot != -1:
    print("Pivot found at index", pivot)
else:
    print("No pivot found")

####SCHOOLED INTERVIEW SOLUTION

def solution(A):
    sum_left = A[0]
    sum_right = sum(A) - A[0]

    diff = abs(sum_left - sum_right)
    
    for i in range(1, len(A) - 1):
        sum_left += A[i]
        sum_right -= A[i]

        current_diff = abs(sum_left -  sum_right)
        if diff > current_diff:
            diff = current_diff

    return diff

print(solution([3,1,2,4,3,9,18,12,19]))