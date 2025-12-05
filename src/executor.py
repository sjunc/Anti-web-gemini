import os
import base64
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from .parser import Action

console = Console()

class Executor:
    def execute(self, action: Action):
        if action.type == 'file':
            self._handle_file(action)
        elif action.type == 'cmd':
            self._handle_cmd(action)
        elif action.type == 'asset':
            self._handle_asset(action)

    def _handle_file(self, action: Action):
        path = action.attributes.get('path')
        # Normalize path
        target_path = os.path.abspath(path)
        content = action.content
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        console.print(f"[bold green]WRITE[/bold green] -> {target_path}")
        try:
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(content)
            console.print("  [dim]Success[/dim]")
        except Exception as e:
            console.print(f"  [bold red]Error writing file:[/bold red] {e}")

    def _handle_cmd(self, action: Action):
        cmd = action.content
        context = action.attributes.get('context', 'local')
        
        # Airlock UI
        console.print()
        console.print(Panel(
            f"[bold white]{cmd}[/bold white]",
            title=f"[bold red]⚠ Airlock Warning: Execute Command? ({context})[/bold red]",
            border_style="red"
        ))
        
        if Confirm.ask("Authorize Execution?"):
            try:
                result = subprocess.run(
                    cmd, 
                    shell=True, 
                    capture_output=True, 
                    text=True,
                    cwd=os.getcwd()
                )
                if result.stdout:
                    console.print(result.stdout)
                if result.stderr:
                    console.print(f"[red]{result.stderr}[/red]")
            except Exception as e:
                console.print(f"[bold red]Execution failed:[/bold red] {e}")
        else:
            console.print("[dim]Skipped[/dim]")

    def _handle_asset(self, action: Action):
        path = action.attributes.get('path')
        target_path = os.path.abspath(path)
        content_b64 = action.content
        
        # Ensure dir
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        console.print(f"[bold magenta]ASSET[/bold magenta] -> {target_path}")
        try:
            # Decode base64
            data = base64.b64decode(content_b64)
            with open(target_path, 'wb') as f:
                f.write(data)
            console.print("  [dim]Saved (Binary)[/dim]")
        except Exception as e:
            console.print(f"  [bold red]Error saving asset:[/bold red] {e}")
