import os

# Default folders to ignore to save tokens and avoid noise
IGNORE_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'node_modules', '.idea', '.vscode'}
# Image/Binary extensions to skip (unless we want to base64 them later, but for now skip text-packer)
IGNORE_EXTS = {'.png', '.jpg', '.jpeg', '.pyc', '.exe', '.dll', '.so'}

def pack_context(root_dir: str) -> str:
    """
    Walks the root_dir and creates a single XML block containing all text files.
    Skips ignored directories and binary extensions.
    """
    output = ["<project_state>"]
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modify dirnames in-place to skip ignored directories (Standard os.walk behavior)
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        # Defense in Depth: If os.walk (or a mock) yields a directory inside an ignored one, skip it.
        # Check if any parent directory is in IGNORE_DIRS
        rel_dir = os.path.relpath(dirpath, root_dir)
        path_parts = rel_dir.split(os.sep)
        if any(part in IGNORE_DIRS for part in path_parts):
            continue
        
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in IGNORE_EXTS:
                continue
                
            full_path = os.path.join(dirpath, filename)
            # Create a relative path for the tag
            rel_path = os.path.relpath(full_path, root_dir).replace('\\', '/')
            
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                output.append(f'<file path="{rel_path}">')
                output.append(content)
                output.append('</file>')
            except UnicodeDecodeError:
                # Skip binary files that tricked the extension check
                pass
            except Exception:
                # Skip unreadable files
                pass
                
    output.append("</project_state>")
    return "\n".join(output)
