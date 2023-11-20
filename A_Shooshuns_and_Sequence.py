def min_operations_to_same_numbers(n, k, sequence,count,ans):
    if count == 0 and sum(sequence) / n != sequence[0]:
        return -1
    elif sum(sequence) / n == sequence[0]:
        return ans
    else:
        a = sequence[k]
        b = sequence[1:]
        b.append(a)
        return min_operations_to_same_numbers(n,k,b,count - 1,ans + 1)

n, k = map(int, input().split())
sequence = list(map(int, input().split()))

result = min_operations_to_same_numbers(n, k - 1, sequence,n,0)
print(result)
