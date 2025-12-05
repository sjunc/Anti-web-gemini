import sys
import argparse
from rich.console import Console
from .parser import Parser
from .executor import Executor

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Antigravity Local CLI")
    parser.add_argument('input_file', nargs='?', help="Path to input file containing Gemini XML. If empty, reads from stdin.")
    parser.add_argument('-d', '--daemon', action='store_true', help="Run in Daemon mode (Watch Clipboard)")
    args = parser.parse_args()

    if args.daemon:
        from .daemon import ClipboardWatcher
        watcher = ClipboardWatcher()
        watcher.start()
        return

    content = ""
    if args.input_file:
        try:
            with open(args.input_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            console.print(f"[bold red]Error reading file:[/bold red] {e}")
            return
    else:
        # Read from stdin
        if sys.stdin.isatty():
             console.print("[yellow]Paste Gemini XML output below (Ctrl+Z/Ctrl+D to finish):[/yellow]")
        content = sys.stdin.read()

    if not content:
        console.print("[red]No content received.[/red]")
        return

    # Parse
    p = Parser()
    actions = p.parse(content)
    
    if not actions:
        console.print("[yellow]No <file> or <cmd> blocks found.[/yellow]")
        return

    console.print(f"[bold blue]Found {len(actions)} actions.[/bold blue]")

    # Execute
    runner = Executor()
    for action in actions:
        runner.execute(action)

if __name__ == "__main__":
    main()
