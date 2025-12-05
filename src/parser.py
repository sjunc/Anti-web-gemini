import re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Action:
    type: str  # 'file' or 'cmd'
    content: str
    attributes: dict

class Parser:
    def __init__(self):
        # Regex for <file> tag: <file path="..." action="...">content</file>
        # Dotall matches newlines
        self.file_pattern = re.compile(
            r'<file\s+path="([^"]+)"(?:\s+action="([^"]+)")?>\n?(.*?)\n?</file>', 
            re.DOTALL
        )
        
        # Regex for <cmd> tag: <cmd context="...">content</cmd>
        self.cmd_pattern = re.compile(
            r'<cmd(?:\s+context="([^"]+)")?>\n?(.*?)\n?</cmd>', 
            re.DOTALL
        )

        # Regex for <asset> tag: <asset type="..." path="...">content</asset>
        self.asset_pattern = re.compile(
            r'<asset\s+type="([^"]+)"\s+path="([^"]+)">\n?(.*?)\n?</asset>',
            re.DOTALL
        )

    def parse(self, text: str) -> List[Action]:
        actions = []
        
        # We need to parse strictly in order of appearance? 
        # Or just find all blocks.
        # Finding all blocks by iteration might be safer to preserve order if mixed.
        # But commonly they are blocks. Let's try to find them by iterating through the string
        # or just finding all iterators and sorting by start index.
        
        file_matches = [
            {
                'type': 'file',
                'start': m.start(),
                'match': m
            } 
            for m in self.file_pattern.finditer(text)
        ]
        
        cmd_matches = [
            {
                'type': 'cmd',
                'start': m.start(),
                'match': m
            } 
            for m in self.cmd_pattern.finditer(text)
        ]

        asset_matches = [
            {
                'type': 'asset',
                'start': m.start(),
                'match': m
            } 
            for m in self.asset_pattern.finditer(text)
        ]
        
        all_matches = sorted(file_matches + cmd_matches + asset_matches, key=lambda x: x['start'])
        
        for item in all_matches:
            m = item['match']
            if item['type'] == 'file':
                path = m.group(1)
                action = m.group(2) or "write"
                content = m.group(3)
                actions.append(Action(
                    type='file',
                    content=content,
                    attributes={'path': path, 'action': action}
                ))
            elif item['type'] == 'cmd':
                context = m.group(1) or "local"
                content = m.group(2).strip()
                actions.append(Action(
                    type='cmd',
                    content=content,
                    attributes={'context': context}
                ))
            elif item['type'] == 'asset':
                m = item['match']
                asset_type = m.group(1)
                path = m.group(2)
                content = m.group(3).strip()
                actions.append(Action(
                    type='asset',
                    content=content,
                    attributes={'path': path, 'type': asset_type}
                ))
                
        return actions
