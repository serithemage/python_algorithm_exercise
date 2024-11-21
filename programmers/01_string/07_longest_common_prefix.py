# 문자열 배열에서 가장 긴 공통 접두사를 찾는 함수
def longest_common_prefix(strs):
    # 빈 배열인 경우 빈 문자열 반환
    if not strs:
        return ""
        
    # 가장 짧은 문자열을 기준으로 비교
    shortest = min(strs, key=len)
    
    # 가장 짧은 문자열의 각 문자를 다른 모든 문자열과 비교
    for i, char in enumerate(shortest):
        for other in strs:
            # 다른 문자를 발견하면 여기까지의 접두사 반환
            if other[i] != char:
                return shortest[:i]
    
    # 모든 비교가 끝나면 가장 짧은 문자열 전체가 공통 접두사
    return shortest

import pytest

def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
