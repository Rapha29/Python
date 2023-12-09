import tkinter as tk
import random
import winsound

# Function to play sound
def play_sound():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000  # Set duration to 1000 milliseconds (1 second)
    winsound.Beep(frequency, duration)

# Function to update score and play sound if computer wins
def update_score(result):
    global player_score, computer_score
    if result == "Empate!":
        pass
    elif result == "Você ganhou!":
        player_score += 1
    else:
        computer_score += 1
        play_sound()  # Play sound if computer wins
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
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    PAPEL
    """,
    "Tesoura": """
    _______
    ---'   ____)____
              ______)
           __________)
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