# 집합 생성
unique_numbers = {1, 2, 3, 4, 5}

# 요소 추가
unique_numbers.add(6)

# 요소 삭제
unique_numbers.remove(3)

# 집합 연산
even_numbers = {2, 4, 6, 8}
intersection = unique_numbers & even_numbers  # {2, 4, 6}

# 요소 갯수
len(unique_numbers)  # 4

import pytest

# 테스트 데이터 초기화
def setup_function():
    # 전역 변수로 선언
    global unique_numbers
    unique_numbers = {1, 2, 3, 4, 5}
def test_set_generation():
    assert unique_numbers == {1, 2, 3, 4, 5}

def test_set_add():
    unique_numbers.add(6)
    assert unique_numbers == {1, 2, 3, 4, 5, 6}

def test_set_remove():
    unique_numbers.remove(3)
    assert unique_numbers == {1, 2, 4, 5}

def test_set_intersection():
    even_numbers = {2, 4, 6, 8}
    intersection = unique_numbers & even_numbers
    assert intersection == {2, 4}

def test_set_len():
    assert len(unique_numbers) == 5
