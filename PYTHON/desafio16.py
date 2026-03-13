from rich import print
from rich import inspect
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

class Funcionario:
    """
    Classe para representar um funcionário de uma empresa.
    """
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentar(self):
        print(f":handshake: Olá, meu nome é [bold blue]{self.nome}[/bold blue], trabalho no setor [bold green]{self.setor}[/bold green] e ocupo o cargo de [bold yellow]{self.cargo}[/bold yellow] da empresa [bold red]MLIMA BIOGAS[/]")

f1 = Funcionario("Icaro", "TI", "Firmware")
f1.apresentar()