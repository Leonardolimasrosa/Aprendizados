from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Console

console = Console()

class ControleRemoto:
    def __init__(self):
        self.tv_ligada = False
        self.volume = 3
        self.canal = 1
        self.max_volume = 5
        self.min_volume = 1
        self.max_canais = 5

    def mostrar_status(self):
        status = "🟢 Ligada" if self.tv_ligada else "🔴 Desligada"

        if self.tv_ligada:
            texto = (
                f"Status: [bold magenta]{status}[/]\n"
                f"Volume: [yellow]{self.volume}[/] {'🔊' * self.volume}\n"
                f"Canal: [yellow]{self.canal}[/]"
            )
        else:
            texto = f"Status: [bold magenta]{status}[/]\n📺 TV Desligada"

        painel = Panel(
            Align.center(texto),
            title="[ TV ]",
            expand=False,
            border_style="bright_magenta",
        )
        console.clear()
        print(painel)

    def ligar_desligar(self):
        self.tv_ligada = not self.tv_ligada

    def volume_mais(self):
        if self.tv_ligada and self.volume < self.max_volume:
            self.volume += 1

    def volume_menos(self):
        if self.tv_ligada and self.volume > self.min_volume:
            self.volume -= 1

    def canal_mais(self):
        if self.tv_ligada:
            self.canal = self.canal + 1 if self.canal < self.max_canais else 1

    def canal_menos(self):
        if self.tv_ligada:
            self.canal = self.canal - 1 if self.canal > 1 else self.max_canais


# -------- PROGRAMA --------
controle = ControleRemoto()

while True:
    controle.mostrar_status()
    comando = input("Digite comando: ").strip()

    if comando == "0":
        print("\n👋 [bold red]Programa encerrado![/]")
        break
    elif comando == "@":
        controle.ligar_desligar()
    elif comando == "+":
        controle.volume_mais()
    elif comando == "-":
        controle.volume_menos()
    elif comando == ">":
        controle.canal_mais()
    elif comando == "<":
        controle.canal_menos()