import pytest
from src.utils.compressor import compress_error

def test_compress_error_shortens_traceback():
    # Simulate a long traceback
    long_traceback = "Traceback (most recent call last):\n"
    for i in range(20):
        long_traceback += f'  File "/site-packages/lib/internal_{i}.py", line {i}, in internal_func\n    pass\n'
    long_traceback += '  File "/user/project/src/main.py", line 10, in <module>\n    1/0\nZeroDivisionError: division by zero'

    compressed = compress_error(long_traceback)
    
    # Assert it's shorter
    assert len(compressed) < len(long_traceback)
    # Assert it kept the user file
    assert "/user/project/src/main.py" in compressed
    # Assert it kept the error message
    assert "ZeroDivisionError" in compressed
    # Assert it removed some internal noise (heuristic)
    assert "internal_5.py" not in compressed
