def is_palindrome(word):
    word_list = list(word)
    word_re = word_list[::-1] 
    if word_list == word_re:
        return True
    return False


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))