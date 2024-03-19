def calculadora():
    while True:
        expressao = input("\nDigite uma expressão matemática ou 'sair' para encerrar: ")
        if expressao.lower() == 'sair':
            print("Calculadora encerrada.\n")
            break

        try:
            resultado = lambda x: eval(x)
            print("Resultado:", resultado(expressao))
        except Exception as e:
            print("Erro:", e)

calculadora()
