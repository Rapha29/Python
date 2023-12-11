import tkinter as tk
import random
import pygame

# Função para reproduzir música
def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Função para atualizar o placar e reproduzir música
def update_score(result):
    global player_score, computer_score
    if result == "Empate!":
        pass
    elif result == "Você ganhou!":
        player_score += 1
        play_music("win.mp3")  # Reproduzir música de vitória
    else:
        computer_score += 1
        play_music("looser.mp3")  # Reproduzir música de derrota
    score_label.config(text=f"Jogador: {player_score}  Computador: {computer_score}")

# Função para o jogo
def rock_paper_scissors(player_choice):
    global player_score, computer_score
    choices = ["Pedra", "Papel", "Tesoura"]
    computer_choice = random.choice(choices)
    
    result = ""
    if player_choice == computer_choice:
        result = "Empate!"
    elif (player_choice == "Pedra" and computer_choice == "Tesoura") or (player_choice == "Papel" and computer_choice == "Pedra") or (player_choice == "Tesoura" and computer_choice == "Papel"):
        result = "Você ganhou!"
    else:
        result = "Você perdeu!"
    
    update_score(result)
    
    # Exibindo a escolha do jogador e do computador em ASCII
    player_choice_label.config(text=f"Escolha do jogador: {ascii_images[player_choice]}")
    computer_choice_label.config(text=f"Escolha do computador: {ascii_images[computer_choice]}")
    
    # Exibindo o resultado do jogo
    result_label.config(text=f"Resultado: {result}")

# Configuração da janela
root = tk.Tk()
root.title("Pedra, Papel, Tesoura")
root.geometry("600x610")

# Dicionário de imagens em ASCII
ascii_images = {
    "Pedra": """
       _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    PEDRA
    """,
    "Papel": """
       _______
    ---'   ____)_____
              _______)
              ________)
             ________)
    ---.___________)
    PAPEL
    """,
    "Tesoura": """
    ---'   ____)______
              ________)
           ___________)
          (____)
    ---.__(___)
    TESOURA
    """
}

# Frame e botões de escolha
options_frame = tk.Frame(root)
options_frame.pack(pady=20)
rock_button = tk.Button(options_frame, text="Pedra", command=lambda: rock_paper_scissors("Pedra"))
rock_button.pack(side="left")
paper_button = tk.Button(options_frame, text="Papel", command=lambda: rock_paper_scissors("Papel"))
paper_button.pack(side="left")
scissors_button = tk.Button(options_frame, text="Tesoura", command=lambda: rock_paper_scissors("Tesoura"))
scissors_button.pack(side="left")

# Rótulos para a escolha do jogador e do computador
player_choice_label = tk.Label(root, text="", font=("Courier", 9))
player_choice_label.pack(pady=20)

computer_choice_label = tk.Label(root, text="", font=("Courier", 9))
computer_choice_label.pack(pady=20)

# Rótulos
score_label = tk.Label(root, text="Jogador: 0  Computador: 0", font=("Arial", 24))
score_label.pack(pady=20)

# Frame para a ilustração
illustration_frame = tk.Frame(root)
illustration_frame.pack(pady=20)

# Rótulo para o resultado
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Variáveis do placar
player_score = 0
computer_score = 0

root.mainloop()