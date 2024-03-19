import pyautogui
import mouse
import time

posicoes_cliques = []

def capturar_posicao_clique(event):
    time.sleep(3)
    posicao = pyautogui.position()
    print(posicao)
    posicoes_cliques.append(posicao)
    

# Registrando o hook para capturar cliques
mouse.hook(capturar_posicao_clique)

try:
    # Mantém o programa em execução para capturar cliques
    while True:
        pass
except KeyboardInterrupt:
    # Se pressionar Ctrl + C, o programa é encerrado
    pass

# Parando a captura do evento do mouse
mouse.unhook_all()

# Ao encerrar o programa, exibe a lista de posições dos cliques
print("Posições dos cliques:")
print(posicoes_cliques)
