from reportlab.pdfgen import canvas

# Solicita ao usuário a opção de investimento ou parcelamento
opcao = input("Deseja investir ou parcelar? ")

# Verifica a opção escolhida pelo usuário e executa o código correspondente
if opcao == "investir":
    # Solicita ao usuário o valor depositado, o rendimento anual em porcentagem e o tempo do investimento em anos
    valor_depositado = float(input("Digite o valor depositado: "))
    rendimento_anual = float(input("Digite o rendimento anual em porcentagem: "))
    tempo_investimento = int(input("Digite o tempo do investimento em anos: "))

    # Converte o rendimento anual em porcentagem para decimal
    rendimento_anual = rendimento_anual / 100

    # Calcula o rendimento mensal
    rendimento_mensal = rendimento_anual / 12

    # Inicializa o valor total do investimento
    valor_total = valor_depositado

    # Cria um objeto PDF
    pdf = canvas.Canvas("investimento.pdf")

    # Adiciona o título do documento
    pdf.drawString(250, 750, "Detalhes de atualização mês a mês do rendimento:")

    # Adiciona as informações de cada mês em uma tabela
    y = 700
    for mes in range(1, tempo_investimento * 12 + 1):
        # Calcula o rendimento do mês
        rendimento_mes = valor_total * rendimento_mensal

        # Atualiza o valor total do investimento
        valor_total += rendimento_mes

        # Adiciona as informações do mês na tabela
        pdf.drawString(50, y, f"Mês {mes}")
        pdf.drawString(150, y, f"Valor total = R${valor_total:.2f}")
        pdf.drawString(300, y, f"Rendimento = R${rendimento_mes:.2f}")
        y -= 20

    # Salva o arquivo PDF
    pdf.save()

elif opcao == "parcelar":
    # Solicita ao usuário o valor, o juros mensal em porcentagem e o tempo do parcelamento em meses
    valor = float(input("Digite o valor: "))
    juros_mensal = float(input("Digite o juros mensal em porcentagem: "))
    tempo_parcelamento = int(input("Digite o tempo do parcelamento em meses: "))

    # Converte o juros mensal em porcentagem para decimal
    juros_mensal = juros_mensal / 100

    # Inicializa o valor total do parcelamento
    valor_total = valor

    # Cria um objeto PDF
    pdf = canvas.Canvas("parcelamento.pdf")

    # Adiciona o título do documento
    pdf.drawString(250, 750, "Detalhes de atualização mês a mês dos juros:")

    # Adiciona as informações de cada mês em uma tabela
    y = 700
    for mes in range(1, tempo_parcelamento + 1):
        # Calcula os juros do mês
        juros_mes = valor_total * juros_mensal

        # Atualiza o valor total do parcelamento
        valor_total += juros_mes

        # Adiciona as informações do mês na tabela
        pdf.drawString(50, y, f"Mês {mes}")
        pdf.drawString(150, y, f"Valor total = R${valor_total:.2f}")
        pdf.drawString(300, y, f"Juros = R${juros_mes:.2f}")
        y -= 20

    # Salva o arquivo PDF
    pdf.save()

else:
    print("Opção inválida. Escolha entre investir ou parcelar.") 