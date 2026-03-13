from rich import print
from rich import inspect
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
import time
install()

class Livro:
    """

    """
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f"Você acabou de abrir o livro '{self.titulo}' que tem {self.paginas} no total. Você está na página {self.pagina_atual}")
    
    def avancar_paginas(self, paginas_avancadas):
        if self.pagina_atual >= self.paginas:
            return
        for i in range(paginas_avancadas):
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} > ", end="")
            else:
                print(f"\nVocê já está na última página do livro '{self.titulo}'")
                break
        print(f"Você avancou {i+1} páginas e agora está na página {self.pagina_atual}")
    
l1 = Livro("O Senhor dos Anéis", 20)
l1.avancar_paginas(10)
l1.avancar_paginas(20)