# 리스트 생성
numbers = [1, 2, 3, 4, 5]

# 요소 추가
numbers.append(6)  # [1, 2, 3, 4, 5, 6]

# 요소 삭제
numbers.remove(3)  # [1, 2, 4, 5, 6]

# 요소 정렬
numbers.sort()  # [1, 2, 4, 5, 6]

# 리스트 뒤집기
numbers.reverse()  # [6, 5, 4, 2, 1]

# 리스트 길이 확인
len(numbers)  # 5

import pytest

# 테스트 데이터 초기화
numbers = [1, 2, 3, 4, 5]

def test_list_generation():
    assert numbers == [1, 2, 3, 4, 5]

def test_list_append():
    numbers.append(6)
    assert numbers == [1, 2, 3, 4, 5, 6]

def test_list_remove():
    numbers.remove(3)
    assert numbers == [1, 2, 4, 5, 6]

def test_list_sort():
    numbers.sort()
    assert numbers == [1, 2, 4, 5, 6]

def test_list_reverse():
    numbers.reverse()
    assert numbers == [6, 5, 4, 2, 1]

def test_list_len():
    assert len(numbers) == 5
    