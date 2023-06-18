def solution(N, A):
    counters = [0] * N  # Initialize all counters to 0
    max_counter = 0  # Track the maximum counter value
    current_max = 0  # Track the current maximum value for optimization

    for operation in A:
        if 1 <= operation <= N:  # Increase the value of a specific counter
            if counters[operation - 1] < max_counter:
                counters[operation - 1] = max_counter
            counters[operation - 1] += 1

            if counters[operation - 1] > current_max:
                current_max = counters[operation - 1]
        elif operation == N + 1:  # Set all counters to the maximum value
            max_counter = current_max

    for i in range(N):  # Apply the final max_counter to any remaining counters
        if counters[i] < max_counter:
            counters[i] = max_counter

    return counters

N = [3,4,4,6,1,4,4]
A = 5
max_counter =  solution(A,N)
print(max_counter)
""""
In this code, we initialize an array called counters with all elements set to 0, representing the counters from 1 to N. We also initialize variables max_counter and current_max.

We iterate through the A array, which contains the operations to be performed. For each operation, we check if it is within the range of 1 to N (inclusive). If so, we increase the value of the corresponding counter and update current_max if necessary. Additionally, if the current counter value is less than the current max_counter, we update it with max_counter to account for the future increment.

If the operation is N + 1, we update max_counter with the current maximum value stored in current_max. This operation sets all counters to the maximum value without individually incrementing each counter.

Finally, we iterate through the counters again and set any remaining counters that are less than max_counter to max_counter.

The time complexity of this solution is O(N + M), where N is the number of counters and M is the length of the A array. The solution performs a single pass through the A array and a final pass through the counters, both of which have linear time complexity.
"""
