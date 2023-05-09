import socket

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
print(f"IP em binário é: {endereco_ip_binario}")

def bin_to_hex(ip_address):
    octets = ip_address.split('.')
    hex_address = ""

    for octet in octets:
        hex_octet = hex(int(octet, 2))[2:]
        hex_address += hex_octet.zfill(2)

    return hex_address

ip_address = endereco_ip_binario
hex_address = bin_to_hex(ip_address)
print(f"Em Hexadecimal fica: {hex_address}")
print(f"Em IPV6 fica ::ffff:{hex_address}")