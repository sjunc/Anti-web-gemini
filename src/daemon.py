import time
import pyperclip
from .parser import Parser
from .executor import Executor
from rich.console import Console

console = Console()

class ClipboardWatcher:
    def __init__(self):
        self.last_content = ""
        self.parser = Parser()
        self.executor = Executor()

    def start(self):
        console.print("[bold green]Antigravity Daemon Started...[/bold green] (Listening to Clipboard)")
        try:
            while True:
                self.tick()
                time.sleep(1)
        except KeyboardInterrupt:
            console.print("\n[bold red]Daemon Stopped.[/bold red]")

    def tick(self):
        try:
            content = pyperclip.paste()
        except:
            return  # Handle clipboard access errors gracefully

        if content == self.last_content:
            return

        self.last_content = content
        
        # Check if it looks like our XML
        if "<file" in content or "<cmd" in content:
            console.print(f"\n[bold magenta]Detected Antigravity Protocol![/bold magenta]")
            actions = self.parser.parse(content)
            if actions:
                for action in actions:
                    self.executor.execute(action)
            else:
                console.print("[dim]Ignored (Invalid XML)[/dim]")
