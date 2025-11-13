from rich.prompt import Prompt
from rich import print

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
            print(f"[green]{dec1} + {dec2} = {dec1 + dec2}[/green]")
        case "-":
            print(f"[green]{dec1} - {dec2} = {dec1 - dec2}[/green]")
        case "*":
            print(f"[green]{dec1} * {dec2} = {dec1 * dec2}[green]")
        case "/":
            if dec2 == 0:
                print(f"{err}: [red]Cannot divide by zero.[/red]")
            else:
                print(f"[green]{dec1} / {dec2} = {dec1 / dec2}[/green]")
        case "**":
            print(f"[green]{dec1 ** dec2}[/green]")
            if dec1 ** dec2 > 2**64:
                print(f"{warn}: [yellow]Result is very large![/yellow]")
        case _:
            print(f"{err}: [red]Invalid operator.[/red]")