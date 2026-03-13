from rich import print
from rich import inspect
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

class Caneta:
    """
    
    """
    def __init__(self, cor):
        self.cor = cor
        self.destampado = False

    def destampar(self):
        if not self.destampado:
            self.destampado = True
    
    def escrever (self, texto):
        if self.destampado:
            print(f"[{self.cor}]{texto}[/]", end="")
        else:
            print(f"\nNão é possível escrever, a caneta [{self.cor}]{self.cor}[/] está tampada!")
        
    def quebrar_linha(self, repeticao):
        for _ in range(repeticao):
            print()
    
c1 = Caneta("blue")
c2 = Caneta("red")

c1.destampar()
c2.destampar()


c1.escrever("Olá, mundo! ")
c1.quebrar_linha(1)
c2.escrever("Python é incrível! ")