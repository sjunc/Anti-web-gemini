import os
from unittest.mock import MagicMock, patch
from src.utils.context_packer import pack_context

@patch('os.walk')
@patch('builtins.open')
def test_pack_context_structure(mock_open, mock_walk):
    # Setup mock file system
    # Root has: src/main.py, .git/HEAD, venv/bin/python
    mock_walk.return_value = [
        ('root', ['src', '.git', 'venv'], ['README.md']),
        ('root/src', [], ['main.py']),
        ('root/.git', [], ['HEAD']),
        ('root/venv', [], ['python'])
    ]
    
    # Mock reading files
    mock_file = MagicMock()
    mock_file.read.return_value = "content"
    # Context manager mock
    mock_open.return_value.__enter__.return_value = mock_file
    
    # Execute
    result = pack_context('root')
    
    # Assertions
    # 1. Should contain README.md
    assert '<file path="README.md">' in result
    # 2. Should contain src/main.py
    assert '<file path="src/main.py">' in result
    # 3. Should NOT contain .git (default ignore)
    assert '.git/HEAD' not in result
    # 4. Should NOT contain venv (default ignore)
    assert 'venv/python' not in result
    # 5. Should be wrapped in root tag
    assert '<project_state>' in result
