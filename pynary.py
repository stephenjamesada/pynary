"""See TODO.md for future implementations"""

from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress
import pyfiglet
import time as t
import random as r

MAX_VALUE = 8
BASE_2_VALUES = "01"
err = "[bold red]Error[/bold red]"
warn = "[bold yellow]Warning[/bold yellow]"

def calculator_mode():
    cm = "[bold](CM) [/bold]"

    def get_binaries():
        while True:
            bin_num1 = str(Prompt.ask(f"[cyan]{cm}Enter binary number 1[/cyan]"))
            num1_len = len(bin_num1)

            bin_num2 = str(Prompt.ask(f"[cyan]{cm}Enter binary number 2[/cyan]"))
            num2_len = len(bin_num2)

            if num1_len > MAX_VALUE or num2_len > MAX_VALUE:
                print(f"{err}: [red]8 digits maximum for both binary numbers.[/red]")
            elif not all(char in BASE_2_VALUES for char in bin_num1) or not all(char in BASE_2_VALUES for char in bin_num2):
                print(f"{err}: [red]Only binary 0 or 1 values are allowed for each number.[/red]")
            else:
                return bin_num1, bin_num2
                break

    bin_num1, bin_num2 = get_binaries()
                
    dec1 = int(bin_num1, 2)
    dec2 = int(bin_num2, 2)

    def get_operator():
        while True:
            operator = Prompt.ask(f"[cyan]{cm}Choose an operator[/cyan]", choices=["+", "-", "*", "/", "**"])
            return operator
            break
                
    operator = get_operator()

    match operator:
        case "+":
            print(f"[green]{bin_num1} + {bin_num2} = {dec1 + dec2}[/green]")
        case "-":
            print(f"[green]{bin_num1} - {bin_num2} = {dec1 - dec2}[/green]")
        case "*":
            print(f"[green]{bin_num1} * {bin_num2} = {dec1 * dec2}[green]")
        case "/":
            if dec2 == 0:
                print(f"{err}: [red]Cannot divide by zero.[/red]")
            else:
                print(f"[green]{bin_num1} / {bin_num2} = {dec1 / dec2}[/green]")
        case "**":
            print(f"[green]{dec1 ** dec2}[/green]")
            if dec1 ** dec2 > 2**64:
                print(f"{warn}: [yellow]Result is very large![/yellow]")
        case _:
            print(f"{err}: [red]Invalid operator.[/red]")

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
        
            calculator_mode()
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