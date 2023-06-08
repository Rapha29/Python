import pandas as pd
import tensorflow as tf
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TFGPT2LMHeadModel

# Inicializar o tokenizador GPT-2 medium
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')

# Criar o modelo GPT-2 medium
model = TFGPT2LMHeadModel.from_pretrained('gpt2-medium')

# Compilar o modelo
model.compile(loss=model.compute_loss, optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5))

# Carregar os dados de treinamento a partir do PDF
with open('meu_arquivo.pdf', 'rb') as file:
    pdf_data = file.read()

# Extrair o texto do PDF usando PyPDF2 ou pdfminer
text_data = ...

# Pré-processar o texto
preprocessed_text = ...

# Tokenizar o texto pré-processado
tokenized_text = tokenizer.encode(preprocessed_text, return_tensors='tf')

# Treinar o modelo
model.fit(tokenized_text, epochs=10, batch_size=32)

# Loop para perguntar e responder
while True:
    # Receber a entrada do usuário
    question = input("Digite sua pergunta: ")

    # Concatenar a pergunta com um separador
    input_text = question + ' [SEP]'

    # Tokenizar a entrada concatenada
    tokenized_input = tokenizer.encode(input_text, return_tensors='tf')

    # Gerar a resposta a partir dos tokens gerados pelo modelo
    output_tokens = model.generate(tokenized_input, max_length=1000, do_sample=True)
    output_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

    # Imprimir a resposta gerada pelo modelo
    print(output_text)