import socket

def ipv4_to_ipv6_nat(ipv4_address):
    ipv4_packed = socket.inet_pton(socket.AF_INET, ipv4_address)
    ipv6_packed = b"\x00" * 10 + b"\xff" * 2 + ipv4_packed
    ipv6_address = socket.inet_ntop(socket.AF_INET6, ipv6_packed)
    return ipv6_address

endereco_ip = input("Digite um IP decimal: ")
ipv4_address = endereco_ip
ipv6_address = ipv4_to_ipv6_nat(ipv4_address)
print(ipv6_address)