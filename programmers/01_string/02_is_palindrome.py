# 회문(Palindrome)이란?
# 앞으로 읽으나 뒤로 읽으나 같은 문자열
# 예) "level", "noon"

# 회문 판별 함수
def is_palindrome(s):
    # 특수문자 및 공백 제거, 소문자로 변환
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

import pytest

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False