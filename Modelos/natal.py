import random
import time

escolha = True
while escolha:
    print("\n")
    print("    Mensagem de Natal")
    print("""
    1. Mensagem 
    0. Exit/Quit/Saída
    """)
    escolha = input("Escolha uma opção:  ")
    
    if escolha == "1":
        mensagens_de_natal = [
            "Feliz Natal! Que esta época seja cheia de alegria e amor.",
            "Desejamos a você um Natal repleto de felicidade e harmonia.",
            "Que o espírito natalino traga paz e esperança para o seu coração.",
            "Neste Natal, compartilhe sorrisos e boas lembranças com a família e amigos.",
            "Que o novo ano que se inicia traga prosperidade e novas conquistas.",
        ]
        mensagem_aleatoria = random.choice(mensagens_de_natal)
        nome_pessoa = input("Digite o nome da pessoa a felicitar: ")
        nome_seu_nome = input("Digite o seu nome: ")
        time.sleep(2)
        print(f"Querido {nome_pessoa}, \n")
        time.sleep(2)
        print(mensagem_aleatoria)
        time.sleep(2)
        print(f"\nUm abraço.\t\t \n{nome_seu_nome} ")
        time.sleep(2)
        
    elif escolha == "0":
        print("Encerrando...")
        break 