def is_palindrome(word):
    for left in range(len(word)//2):
        right = len(word) - left -1
        if word[left] != word[right]:
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))