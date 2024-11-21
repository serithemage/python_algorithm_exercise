# Anagram이란?
# 두 문자열이 서로 다른 문자를 사용하여 구성되어 있는 것
# 예) "listen"과 "silent"는 모두 "l", "i", "s", "t", "e", "n"을 사용하여 구성되어 있으므로 Anagram

# 애너그램 판별 함수
def is_anagram(s1, s2):
    # 방법 1: 정렬 사용
    return sorted(s1) == sorted(s2)
    
    # 방법 2: Counter 사용
    from collections import Counter
    return Counter(s1) == Counter(s2)

import pytest

def test_is_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False