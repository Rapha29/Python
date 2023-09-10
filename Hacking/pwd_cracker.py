import random
import os
import time


def generate_random_password(characters):
    return ''.join(random.choice(characters) for _ in range(len(u_pwd)))

def find_password(characters, method_description):
    start_time = time.time()  
    pw = ''
    while pw != u_pwd:
        pw = generate_random_password(characters)
        elapsed_time = time.time() - start_time
        print(f"Procurando Senha\nTentativa: {pw}\nTempo decorrido: {elapsed_time:.2f} segundos", end='\r')
        os.system('cls' if os.name == 'nt' else 'clear') 
    return pw

if os.path.isfile("senhas.txt"):
    with open("senhas.txt", "r") as file:
        possible_passwords = file.read().split()    
    u_pwd = input("Digite uma senha: ")

    if u_pwd in possible_passwords:
        print(f"A senha é: {u_pwd}")
    else:
        print("Senha não encontrada no arquivo.")
else:
    u_pwd = input("Digite uma senha: ")
    numeros = [str(i) for i in range(10)]
    start_time = time.time()
    pw = find_password(numeros, "números")

    print(f"A senha é: {pw}")
    print(f"Tempo decorrido: {time.time() - start_time:.2f} segundos") 

    u_pwd = input("Digite uma senha: ")
    alfabeto_maiusculo = [chr(i) for i in range(65, 91)] 
    alfabeto_minusculo = [chr(i) for i in range(97, 123)] 
    start_time = time.time()
    pw = find_password(alfabeto_maiusculo + alfabeto_minusculo, "letras")

    print(f"A senha é: {pw}")
    print(f"Tempo decorrido: {time.time() - start_time:.2f} segundos")

    u_pwd = input("Digite uma senha: ")
    start_time = time.time()
    pw = find_password(numeros + alfabeto_maiusculo + alfabeto_minusculo, "números e letras")

    print(f"A senha é: {pw}")
    print(f"Tempo decorrido: {time.time() - start_time:.2f} segundos")

    u_pwd = input("Digite uma senha: ")
    caracteres_especiais = ['!', '@', '#', '$', '%', '&']
    start_time = time.time()
    pw = find_password(numeros + alfabeto_maiusculo + alfabeto_minusculo + caracteres_especiais, "números, letras e caracteres especiais")

    print(f"A senha é: {pw}")
    print(f"Tempo decorrido: {time.time() - start_time:.2f} segundos") 
