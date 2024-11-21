# 문자열의 모든 순열을 반환하는 함수
from itertools import permutations
def get_permutations(s):
    return list(map(''.join, permutations(s)))

import pytest

def test_get_permutations():
    assert get_permutations("abc") == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']