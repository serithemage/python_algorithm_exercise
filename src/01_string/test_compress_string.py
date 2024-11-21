# 문자열 압축 함수
def compress_string(s):
    if not s:
        return ""
        
    result = []
    count = 1
    current = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            result.append(current + str(count))
            current = s[i]
            count = 1
            
    result.append(current + str(count))
    compressed = ''.join(result)
    
    return compressed if len(compressed) < len(s) else s

import pytest

def test_compress_string():
    assert compress_string("aabbbcccc") == "a2b3c4"