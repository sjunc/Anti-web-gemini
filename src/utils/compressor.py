def compress_error(traceback_str: str) -> str:
    """
    Compresses a traceback by removing generic library frames.
    Keeps:
    1. The header "Traceback..."
    2. Frames that do NOT contain 'site-packages' or 'dist-packages'
    3. The final Error line.
    """
    lines = traceback_str.split('\n')
    compressed_lines = []
    
    # Always keep the first line (Traceback header)
    if lines:
        compressed_lines.append(lines[0])
    
    # Iterate through middle lines (frames)
    # This is a simple heuristic. A more robust one would parse the traceback structure.
    # But for text reduction, line filtering is fast.
    for line in lines[1:-1]:
        # Keep if it doesn't look like a library path
        if "site-packages" not in line and "dist-packages" not in line:
            compressed_lines.append(line)
        # Or if it's the actual code line (usually indented, follows a File line)
        # We might want to be careful here. 
        # Actually, standard traceback is:
        #   File "...", line ..., in ...
        #     code
        # We should keep pairs.
    
    # For now, let's just filter file lines based on path, and keep code lines if previous file line was kept.
    # Re-impl with state
    
    final_lines = []
    if lines:
        final_lines.append(lines[0])
        
    keep_next = False
    for i in range(1, len(lines)-1):
        line = lines[i]
        if line.strip().startswith('File "'):
            if "site-packages" not in line and "dist-packages" not in line and "<frozen" not in line:
                final_lines.append(line)
                keep_next = True
            else:
                keep_next = False
        elif keep_next:
            final_lines.append(line)
            
    # Always keep the last line (The Exception)
    if len(lines) > 1:
        final_lines.append(lines[-1])
        
    return '\n'.join(final_lines)
