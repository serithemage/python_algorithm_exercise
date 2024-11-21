# 중복되지 않는 가장 긴 부분 문자열의 길이를 찾는 함수
def longest_substring_without_repeating(s):
    char_index = {}
    max_length = start = 0
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        char_index[char] = i
        
    return max_length

import pytest

def test_longest_substring_without_repeating():
    assert longest_substring_without_repeating("abcabcbb") == 3