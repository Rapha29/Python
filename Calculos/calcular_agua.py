import math

def beber_agua():
    peso = float(input("Digite o seu peso em kg: "))
    hora_acordar = int(input("Digite a hora que você acorda (em horas): "))
    hora_dormir = int(input("Digite a hora que você vai dormir (em horas): "))

    quantidade_total = peso * 35  # Calcula a quantidade total de água em ml
    horas_acordado = hora_dormir - hora_acordar  # Calcula o número de horas que a pessoa estará acordada
    doses_diarias = quantidade_total / 200  # Calcula o número de doses diárias
    quantidade_litros = quantidade_total / 1000
    doses_por_dia = math.ceil(doses_diarias)  # Arredonda o número de doses para cima
    print(f"Você deve beber {quantidade_litros:.1f} litros de água durante o dia.")
    print(f"Você deve beber {doses_por_dia} copos de água (200ml cada) durante o dia.\n")

    # Calcula o intervalo de tempo entre as doses
    horas_acordado = hora_dormir - hora_acordar  # Calcula o número de horas que a pessoa estará acordada
    intervalo_minutos = (horas_acordado * 60) / doses_por_dia
    print(f"Você permanece acordado(a) em média {horas_acordado} horas durante o dia.\n")

    # Calcula o intervalo entre o copos de água a serem tomados
    hora_atual = hora_acordar
    for i in range(doses_por_dia):
        minutos = int((hora_atual % 1) * 60)
        if minutos >= 60:  # Garante que os minutos não ultrapassem 59
            minutos = 59
        print(f" -> 🥛 Tome um copo de água às {hora_atual:02.0f}:{minutos:02d}")
        hora_atual += intervalo_minutos / 60

beber_agua()

