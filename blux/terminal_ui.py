from rich.console import Console

class TerminalUI:
    def __init__(self, ai_engine, memory):
        self.console = Console()
        self.ai_engine = ai_engine
        self.memory = memory

    def run(self):
        self.console.print("[bold cyan]BLUX Terminal Ready.[/bold cyan]")
        while True:
            try:
                prompt = self.console.input("[green]>>> [/green]")
                if prompt.lower() in ["exit", "quit"]:
                    break
                elif prompt == "/recall notes":
                    notes = self.memory.get_notes()
                    self.console.print(notes)
                elif prompt.startswith("/note "):
                    note = prompt[6:]
                    self.memory.add_note(note)
                    self.console.print(f"Note saved: {note}")
                else:
                    response = self.ai_engine.query(prompt)
                    self.console.print(f"[bold yellow]{response}[/bold yellow]")
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")

