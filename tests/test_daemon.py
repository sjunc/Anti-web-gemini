from unittest.mock import MagicMock, patch
from src.daemon import ClipboardWatcher

@patch('src.daemon.pyperclip.paste')
@patch('src.daemon.Parser')
@patch('src.daemon.Executor')
@patch('src.daemon.time.sleep')
def test_daemon_triggers_on_xml(mock_sleep, mock_executor, mock_parser, mock_paste):
    # Setup
    watcher = ClipboardWatcher()
    
    # 1. No XML
    mock_paste.return_value = "Just some text"
    watcher.tick() # One loop iteration
    mock_parser.return_value.parse.assert_not_called()
    
    # 2. XML Detected
    xml_content = '<cmd>echo hello</cmd>'
    mock_paste.return_value = xml_content
    
    # Mock parser output
    mock_action = MagicMock()
    mock_parser.return_value.parse.return_value = [mock_action]
    
    watcher.tick()
    
    mock_parser.return_value.parse.assert_called_with(xml_content)
    mock_executor.return_value.execute.assert_called_with(mock_action)
