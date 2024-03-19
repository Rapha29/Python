import speedtest # pip install speedtest-cli

def testar_velocidade_internet():
    st = speedtest.Speedtest()
    print("Testando velocidade de download...")
    velocidade_download = st.download() / 1_000_000  # convertendo para Mbps
    print(f"Velocidade de download: {round(velocidade_download, 2)} Mbps")

    print("Testando velocidade de upload...")
    velocidade_upload = st.upload() / 1_000_000  # convertendo para Mbps
    print(f"Velocidade de upload: {round(velocidade_upload, 2)} Mbps")

    servidor = st.get_best_server()
    print(f"Latência: {servidor['latency']} ms")

if __name__ == "__main__":
    testar_velocidade_internet()
