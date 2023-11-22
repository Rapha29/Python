import subprocess

def instalar_pacotes():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("Pacotes instalados com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro durante a instalação dos pacotes: {e}")

if __name__ == "__main__":
    instalar_pacotes()