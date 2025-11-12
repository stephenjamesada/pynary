"""See TODO.md for future implementations"""

from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress
import pyfiglet
import time as t
import random as r
import calculator_mode as cal_mode

MAX_VALUE = 8
BASE_2_VALUES = "01"
err = "[bold red]Error[/bold red]"

def title():
    title_text = pyfiglet.figlet_format("Pynary", font="slant")
    panel_title = "[bold green]Binary to decimal conversion[/bold green]"
    panel_subtitle = "[dim green]Made by [link=https://github.com/stephenjamesada]stephenjamesada[/link][/dim green]"
    print(Panel.fit(f"[green]{title_text}[/green]",
        title=panel_title,
        subtitle=panel_subtitle))
    t.sleep(1)

try:
    title()
    while True:
        binary = str(Prompt.ask("[cyan]Enter a binary number (q to quit, cm for calculator mode)[/cyan]"))
        length = len(binary)
       
       # Key interactions
        if binary == 'q':
            print("[green]Goodbye![/green]")
            break
        elif binary == 'cm':
            progress = Progress()
            progress.start()
            task = progress.add_task("[bold magenta]Entering Calculator Mode...[/bold magenta]", total=100)
            
            for i in range(100):
                t.sleep(r.uniform(0.015625, 0.0625))
                progress.update(task, advance=1)

            progress.stop()
        
            cal_mode.calculator_mode()
            continue

        if length > MAX_VALUE:
            print(f"{err}: [red]8 digits maximum.[/red]")
            continue
        elif not all(char in BASE_2_VALUES for char in binary):
            print(f"{err}: [red]Only binary 0 or 1 values are allowed.[/red]")
            continue
        else:
            decimal = int(binary, 2)
            print(f"[green]{decimal}[/green]")
except KeyboardInterrupt:
    print("[green]\nGoodbye![/green]")