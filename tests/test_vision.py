import base64
import os
from unittest.mock import MagicMock, patch
from src.parser import Parser, Action
from src.executor import Executor

def test_parser_extracts_asset():
    xml = '<asset type="image" path="test_image.png">SGVsbG8=</asset>' # Hello in base64
    parser = Parser()
    actions = parser.parse(xml)
    
    # Current parser won't find it yet
    assert len(actions) == 1
    assert actions[0].type == 'asset'
    assert actions[0].attributes['path'] == 'test_image.png'
    assert actions[0].content.strip() == 'SGVsbG8='

@patch('builtins.open')
def test_executor_writes_asset(mock_open):
    executor = Executor()
    action = Action(
        type='asset',
        content='SGVsbG8=', # Hello
        attributes={'path': 'test_image.png'}
    )
    
    # Mock binary write
    mock_file = MagicMock()
    mock_open.return_value.__enter__.return_value = mock_file
    
    executor.execute(action)
    
    mock_open.assert_called_with(os.path.abspath('test_image.png'), 'wb')
    mock_file.write.assert_called_with(b'Hello')
