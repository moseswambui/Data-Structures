"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

class Solution { public int solution(int X, int[] A); }

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""

def solution(X,A):
  covered = [False] * (X + 1)
  uncovered_count = X

  for second, position in enumerate(A):
    if not covered[position]:
      covered[position] = True
      uncovered_count -= 1

      if uncovered_count == 0:
        return second
      
  return -1

X = 5
A = [1,4,2,3,5,4]

earliest_time = solution(X, A)
print("Earliest Time: ", earliest_time)

"""
In this code, we start by initializing a boolean list called covered with False values, representing the positions across the river. We also initialize uncovered_count to the total number of positions that need to be covered.

We then iterate through the A array, which contains the positions where leaves fall at each second. For each second, we check if the position is already covered. If it's not covered, we mark it as covered, decrement the uncovered_count by 1, and check if all positions are now covered (uncovered_count == 0). If so, we return the current second as the earliest time when the frog can jump to the other side.

If the frog is never able to jump to the other side, the function will return -1.

The time complexity of this solution is O(N), where N is the length of the A array. This is because we iterate through the array once, and the operations within the loop are constant time.

"""

###CODILITY

def solution(x, a):
  river_position = [False] * (x + 1)

  for time in range(len(a)):
    pos = a[time]
    if not river_position[pos]:
      river_position[pos] = True
      x -= 1

      if x==0:
        return time
      
  return -1

print(solution(9, [1,4,2,3,5,4,1]))