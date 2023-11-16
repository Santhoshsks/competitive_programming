def is_palindrome(s):
    return s == s[::-1]

def game_winner(s):
    if is_palindrome(s):

        return "First"
    elif len(s) % 2 == 0 or s.count(s[0]) == len(s):

        return "Second"
    else:
        return "First"
    
s = input().strip()
print(game_winner(s))
