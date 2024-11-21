# 문자열 뒤집기
def reverse_string(s):
    # 파이썬의 슬라이싱 기능을 사용하여 문자열을 역순으로 반환
    # s[시작:끝:스텝] 에서 스텝을 -1로 지정하면 역순으로 슬라이싱됨
    return s[::-1]

import pytest

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
