def calcular_quilometragem_de_pinto(idade_inicial, idade_atual):
    tamanho_medio_cm = 15
    duracao_media_minutos = 10
    vezes_por_segundo = 1
    vezes_por_semana = 5
    anos_ativos = idade_atual - idade_inicial
    semanas_ativas = anos_ativos * 52

    distancia_total_km = (
        (tamanho_medio_cm / 100) *
        duracao_media_minutos *
        vezes_por_segundo *
        vezes_por_semana *
        semanas_ativas
    )

    return distancia_total_km

idade_inicial = 20
idade_atual = 30

quilometragem = calcular_quilometragem_de_pinto(idade_inicial, idade_atual)
print(f"A pessoa levou aproximadamente {quilometragem:.2f} quilômetros de pinto.")