from rich.console import Console
import re

class InputValidator:
    """Centralized input validation"""
    
    @staticmethod
    def validate_prompt(prompt):
        """Validate user prompt input"""
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string")
        
        # Length limits
        if len(prompt) > 2048:
            raise ValueError("Input too long (max 2048 characters)")
        
        if len(prompt.strip()) == 0:
            raise ValueError("Input cannot be empty")
        
        # Check for suspicious patterns
        suspicious_patterns = [
            r'<script[^>]*>',  # Script tags
            r'javascript:',    # JavaScript URLs
            r'data:',          # Data URLs
            r'vbscript:',      # VBScript URLs
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                raise ValueError("Input contains suspicious content")
        
        return prompt.strip()
    
    @staticmethod
    def validate_note(note):
        """Validate note input"""
        if not isinstance(note, str):
            raise ValueError("Note must be a string")
        
        if len(note) > 1024:
            raise ValueError("Note too long (max 1024 characters)")
        
        return note.strip()

class TerminalUI:
    def __init__(self, ai_engine, memory):
        self.console = Console()
        self.ai_engine = ai_engine
        self.memory = memory
        self.validator = InputValidator()

    def run(self):
        self.console.print("[bold cyan]BLUX Terminal Ready.[/bold cyan]")
        self.console.print("[dim]Type 'help' for commands, 'exit' to quit.[/dim]")
        
        while True:
            try:
                prompt = self.console.input("[green]>>> [/green]")
                
                if prompt.lower() in ["exit", "quit"]:
                    break
                elif prompt.lower() == "help":
                    self.show_help()
                elif prompt == "/recall notes":
                    self.recall_notes()
                elif prompt.startswith("/note "):
                    self.add_note(prompt[6:])
                else:
                    self.process_ai_query(prompt)
                    
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Use 'exit' to quit.[/yellow]")
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")
    
    def show_help(self):
        """Display help information"""
        help_text = """
[bold cyan]BLUX Commands:[/bold cyan]
  help              - Show this help
  exit, quit        - Exit BLUX
  /note <text>      - Save a note
  /recall notes     - Show saved notes
  <anything else>   - Send to AI engine
        """
        self.console.print(help_text)
    
    def recall_notes(self):
        """Safely recall notes"""
        try:
            notes = self.memory.get_notes()
            if notes:
                self.console.print("[bold yellow]Saved Notes:[/bold yellow]")
                for i, note in enumerate(notes, 1):
                    # Escape note content for safe display
                    safe_note = str(note).replace('[', '\\[')
                    self.console.print(f"  {i}. {safe_note}")
            else:
                self.console.print("[dim]No notes saved.[/dim]")
        except Exception as e:
            self.console.print(f"[red]Error retrieving notes: {e}[/red]")
    
    def add_note(self, note_text):
        """Safely add a note"""
        try:
            validated_note = self.validator.validate_note(note_text)
            self.memory.add_note(validated_note)
            self.console.print(f"[green]Note saved: {validated_note}[/green]")
        except ValueError as e:
            self.console.print(f"[red]Invalid note: {e}[/red]")
        except Exception as e:
            self.console.print(f"[red]Error saving note: {e}[/red]")
    
    def process_ai_query(self, prompt):
        """Safely process AI query"""
        try:
            validated_prompt = self.validator.validate_prompt(prompt)
            response = self.ai_engine.query(validated_prompt)
            # Escape response for safe display
            safe_response = str(response).replace('[', '\\[')
            self.console.print(f"[bold yellow]{safe_response}[/bold yellow]")
        except ValueError as e:
            self.console.print(f"[red]Invalid input: {e}[/red]")
        except Exception as e:
            self.console.print(f"[red]Error processing query: {e}[/red]")

