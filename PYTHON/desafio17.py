from rich import print
from rich import inspect
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}\n"
        conteudo += f"{'-' * 30}\n"
        precoMensagem = f"R${self.preco:,.2f}"
        conteudo += f"{precoMensagem.center(30, '.')}"
        etiqueta = Panel(conteudo,
                         title="Produto", 
                         style="bold yellow",
                         height=5,
                         expand=False,
                         border_style="bold blue")
        print(etiqueta)

p1 = Produto("Smartphone", 1999.99)
p2 = Produto("Notebook", 3499.99)
p3 = Produto("Fone de Ouvido", 299.99)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()