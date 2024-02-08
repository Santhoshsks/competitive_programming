def find_string_from_trace(trace):
    n = len(trace)
    s = ['a'] * n
    last_occurrence = {}

    for i in range(n):
        if trace[i] == 0:
            continue
        if trace[i] - 1 in last_occurrence:
            char = s[last_occurrence[trace[i] - 1]]
            s[i] = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        last_occurrence[trace[i]] = i

    return ''.join(s)

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        trace = list(map(int, input().strip().split()))
        print(find_string_from_trace(trace))

if __name__ == "__main__":
    main()
