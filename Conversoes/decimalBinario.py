def decimal_para_binario(decimal):
    if decimal == 0:
        return "00000000"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    binario = "0" * (8 - len(binario)) + binario
    return binario
endereco_ip = input("Digite um IP decimal): ")
octetos_decimal = endereco_ip.split(".")
octetos_binario = [decimal_para_binario(int(octeto)) for octeto in octetos_decimal]
endereco_ip_binario = ".".join(octetos_binario)
print(f"IP em binário é {endereco_ip_binario}")