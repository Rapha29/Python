import os
import subprocess
from reportlab.pdfgen import canvas

# Obtenha o caminho absoluto do diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Localize o arquivo .dbk na pasta atual
dbk_file = None
for file in os.listdir(current_dir):
    if file.endswith('.dbk'):
        dbk_file = os.path.join(current_dir, file)
        break

if dbk_file is None:
    print("Arquivo .dbk não encontrado na pasta atual.")
else:
    # Componha o comando pydbk para extrair o arquivo .dbk
    command = ['pydbk', dbk_file, current_dir]

    # Execute o comando pydbk usando subprocess
    subprocess.run(command, capture_output=True)

    # Gere um arquivo PDF com o mesmo nome do arquivo .dbk
    pdf_file = os.path.splitext(os.path.basename(dbk_file))[0] + '.pdf'
    pdf_path = os.path.join(current_dir, pdf_file)

    # Crie um documento PDF usando o ReportLab
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Arquivo PDF gerado a partir do arquivo .dbk")
    c.save()

    print(f"Arquivo PDF '{pdf_file}' gerado com sucesso.")
