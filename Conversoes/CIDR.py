import ipaddress

cidr = input("IP/CIDR: ")
rede = ipaddress.ip_network(cidr, strict=False)

print("Endereço de rede: ", rede.network_address)
print("Máscara de sub-rede: ", rede.netmask)
print("Broadcast: ", rede.broadcast_address)
print("Quantidade de hosts totais: ", rede.num_addresses)
print("Quantidade de hosts válidos: ", rede.num_addresses - 2)