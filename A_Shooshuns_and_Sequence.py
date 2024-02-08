# Import deque and Counter from collections module
from collections import deque, Counter

# Read the input
n, k = map(int, input().split())
sequence = deque(map(int, input().split()))

# Initialize the number of operations and the counter
ops = 0
counter = Counter(sequence)

# Loop through the sequence from the end
for i in range(n - 1, -1, -1):
    # If the current element is not equal to the last element
    if sequence[i] != sequence[-1]:
        # If the current element is the k-th element
        if i == k - 1:
            # Add the same element to the end of the sequence
            sequence.append(sequence[i])
            # Delete the first element of the sequence
            sequence.popleft()
            # Increment the number of operations
            ops += 1
            # Update the counter
            counter[sequence[i]] += 1
            counter[sequence[i + 1]] -= 1
        # Otherwise, it is impossible to make all numbers the same
        else:
            # Print -1 and exit the loop
            print(-1)
            break
    # If the counter has only one key
    elif len(counter) == 1:
        # Print the number of operations and exit the loop
        print(ops)
        break
