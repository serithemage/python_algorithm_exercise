# 튜플 생성
coordinates = (10, 20)

# 인덱스로 접근
x = coordinates[0]  # 10
y = coordinates[1]  # 20

import pytest

def test_tuple_generation():
    assert coordinates == (10, 20)

def test_tuple_access():
    assert coordinates[0] == 10
    assert coordinates[1] == 20
