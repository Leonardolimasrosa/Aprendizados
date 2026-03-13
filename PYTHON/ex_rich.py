# Para usar a documentação completa do RICH, entre no site rich.readthedocs.io e veja
# E para emojis, no terminal escreva "python -m rich.emoji" e para usa-los, basta colocar o nome do emoji entre dois pontos
from rich import print # Torna a função print mais poderosa, permitindo formatação de texto, cores e emojis
from rich import inspect # Permite inspecionar objetos e exibir suas informações de forma legível
from rich.panel import Panel # Permite criar painéis para destacar informações
from rich.table import Table # Permite criar tabelas formatadas para exibir dados de forma organizada
from rich.traceback import install # Instala um formatador de erro, onde torna mais fácil investigar o erro no código
install() # Ativa o formatador de erro do RICH

painel = Panel("Aqui estão exemplos dos recursos do [bgcolor blue]RICH[/]", # O conteúdo do painel, que pode ser texto ou outros elementos do RICH
                title="Painel de Exemplo", # Define um título para o painel
                  subtitle="Subtítulo do Painel", # Define um subtítulo para o painel
                  style="bold magenta", # Define a cor e o estilo do painel
                  width=50, # Define a largura do painel
                  padding=(1, 3), # Define o preenchimento interno do painel (top, right, bottom, left) ou (top, bottom)
                    border_style="bright_blue") # Define o estilo da borda do painel

tabela = Table(title="Tabela de Exemplo")
tabela.add_column("ID", justify="center", style="blue")
tabela.add_column("Nome", justify="center", style="green")
tabela.add_column("Saldo", justify="center", style="red")
tabela.add_row("1", "João", "R$ 1.500,00")
tabela.add_row("2", "Maria", "R$ 2.000,00")
tabela.add_row("3", "Pedro", "R$ 500,00")

print(painel)
print(tabela)