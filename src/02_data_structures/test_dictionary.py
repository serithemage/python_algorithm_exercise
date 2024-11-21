# 딕셔너리 생성
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# 값 추가 또는 수정
student_scores['David'] = 90

# 값 삭제
del student_scores['Alice']

# 값 접근
print(student_scores['Bob'])  # 92

import pytest

# 테스트 데이터 초기화
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

def test_dictionary_generation():
    assert student_scores == {'Alice': 85, 'Bob': 92, 'Charlie': 78}

def test_dictionary_add_or_update():
    student_scores['David'] = 90
    assert student_scores == {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}

def test_dictionary_delete():
    del student_scores['Alice']
    assert student_scores == {'Bob': 92, 'Charlie': 78, 'David': 90}

def test_dictionary_access():
    assert student_scores['Bob'] == 92
