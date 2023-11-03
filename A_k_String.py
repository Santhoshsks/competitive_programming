from collections import Counter

def rearrange_string(k, s):
    char_count = Counter(s)

    total_count = sum(char_count.values())
    
    if total_count % k != 0:
        return "-1"

    result = ""
    for char, count in sorted(char_count.items()):
        if count % k != 0:
            return "-1"
        result += char * (count // k)

    result = result * k

    return result

k = int(input())
s = input()

result = rearrange_string(k, s)
print(result)
