from rich import print
from rich import inspect
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

class Churrasco:
    """
    Classe para analisar o custo de um churrasco, considerando o consumo padrão de carne por pessoa e o preço do kg da carne.
     - Atributos:
        - consumo_padrao: Consumo padrão de carne por pessoa (kg).
        - preco_kg: Preço do kg da carne.
     - Métodos:
        - __init__(self, titulo, pessoas): Inicializa a classe com o título do churrasco e o número de convidados.
        - analisar(self): Calcula o total de carne necessária, o custo total e o custo individual, e exibe as informações em um painel formatado.
     - Exemplo de uso:
        c1 = Churrasco("Churrasco de Aniversário", 15)
        c1.analisar()
    """

    consumo_padrao = 0.4 # kg por pessoa
    preco_kg = 82.40


    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas
    
    def analisar(self):
        total_carne = Churrasco.consumo_padrao * self.pessoas
        custo = total_carne * Churrasco.preco_kg
        custo_individual = custo / self.pessoas

        churras = Panel(
        f"Analisando o [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/]\n"
        f"Cada participante comerá {Churrasco.consumo_padrao}Kg e cada custa R${Churrasco.preco_kg:,.2f}\n"
        f"Recomendo [blue]comprar {total_carne:,.3f}Kg[/] de carne\n"
        f"O custo total será de [green]R${custo:,.2f}[/]\n"
        f"Cada pessoa pagará [yellow]R${custo_individual:,.2f}[/] para participar.",
        title=self.titulo,
        expand=False,
        border_style = "bold magenta"
        )
        print(churras)

c1 = Churrasco("Churrasco de Aniversário", 15)
c1.analisar()