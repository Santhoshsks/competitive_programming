from collections import deque, Counter

n, k = map(int, input().split())
sequence = list(map(int, input().split()))

ops = 0
counter = Counter(sequence)

for i in range(n - 1, -1, -1):
    # If the current element is not equal to the last element
    if sequence[i] != sequence[-1]:
        # If the current element is the k-th element
        if i == k - 1:
            # Add the same element to the end of the sequence
            sequence.append(sequence[i])
            # Delete the first element of the sequence
            sequence.pop(0)
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
