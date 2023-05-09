import random

# Define os atributos do jogador
player = {"name": "herói", "health": 100, "attack": 10, "defense": 5}

# Define os monstros e suas propriedades
monsters = [
    {"name": "goblin", "health": 50, "attack": 5, "defense": 2},
    {"name": "ogre", "health": 80, "attack": 8, "defense": 4},
    {"name": "dragon", "health": 150, "attack": 12, "defense": 8},
]

def fight(monster):
    """Realiza uma luta entre o jogador e um monstro."""
    print(f"Um {monster['name']} apareceu!")

    # Loop da luta
    while player["health"] > 0 and monster["health"] > 0:
        # Jogador ataca
        damage_dealt = player["attack"] - monster["defense"]
        if damage_dealt < 0:
            damage_dealt = 0
        monster["health"] -= damage_dealt
        print(f"Você ataca o {monster['name']} e causa {damage_dealt} pontos de dano.")

        # Monstro ataca
        damage_dealt = monster["attack"] - player["defense"]
        if damage_dealt < 0:
            damage_dealt = 0
        player["health"] -= damage_dealt
        print(f"O {monster['name']} ataca você e causa {damage_dealt} pontos de dano.")

        # Imprime o estado atual da luta
        print(f"Você tem {player['health']} pontos de vida restantes.")
        print(f"O {monster['name']} tem {monster['health']} pontos de vida restantes.")

    # Verifica quem ganhou
    if player["health"] <= 0:
        print("Você foi derrotado!")
    else:
        print(f"Você derrotou o {monster['name']}!")

# Loop principal do jogo
while True:
    # Pede para o jogador escolher uma ação
    print("O que você deseja fazer?")
    print("1. Explorar")
    print("2. Descansar")
    choice = input("> ")

    # Exploração
    if choice == "1":
        # Escolhe um monstro aleatoriamente e luta contra ele
        monster = random.choice(monsters)
        fight(monster)

    # Descanso
    elif choice == "2":
        # Recupera um pouco da saúde do jogador
        player["health"] += 10
        print("Você descansa e recupera 10 pontos de vida.")

    # Ação desconhecida
    else:
        print("Ação desconhecida.")