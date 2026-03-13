from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        lista_jogos = "\n".join(f"🕹️ {j}" for j in self.jogos) if self.jogos else "Nenhum jogo adicionado"

        painel = Panel(
            f"👤 Nome real: [green]{self.nome}[/]\n\n"
            f"⭐ Jogos favoritos:\n[yellow]{lista_jogos}[/]",
            title=f"Jogador <{self.nick}>",
            border_style="bright_magenta",
            padding=(1,2),
            expand=False
        )

        print(painel)

g1 = Gamer("Lucas", "Lukinha")
g1.adicionar_jogo("The Legend of Zelda")
g1.adicionar_jogo("Super Mario Odyssey")
g1.adicionar_jogo("Minecraft")
g1.ficha()