import smtplib
import ssl
from flask import Flask, request, render_template

app = Flask(__name__)

users = [
    {"email": "rapha2929@gmail.com", "pass": "rapha123"},
    {"email": "example@example.com", "pass": "examplepass"},
    {"email": "another@example.com", "pass": "anotherpass"}
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_email = request.form["email"]
        user_pass = request.form["Pass"]

        for user in users:
            if user_email == user["email"] and user_pass == user["pass"]:
                return render_template("dashboard.html")

        return render_template("wrong.html")

    return render_template('index.html')


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        user_email = request.form["email"]
        user_pass = request.form["password"]

        # Verificar se o usuário já está cadastrado
        for user in users:
            if user_email == user["email"]:
                return render_template("already_registered.html", email=user_email)

        # Adicionar o novo usuário à lista de usuários
        users.append({"email": user_email, "pass": user_pass})

        return render_template("registration_success.html", email=user_email)

    return render_template("registration_form.html")


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]

        enviar_email(nome, email, telefone, endereco)
        return render_template("enviado.html")

    return render_template("formulario.html")


def enviar_email(nome, email, telefone, endereco):
    remetente = "raphagithub@outlook.com"  # Seu endereço de email
    senha = "Raphagit123"  # Sua senha do email

    destinatario = "rapha2929@gmail.com"  # Endereço de email para onde o email será enviado
    assunto = "Novo formulário preenchido"
    mensagem = f"""
    Nome: {nome}
    Email: {email}
    Telefone: {telefone}
    Endereço: {endereco}
    """

    # Configuração do servidor SMTP com SSL
    contexto = ssl.create_default_context()
    servidor = smtplib.SMTP("smtp-mail.outlook.com", 587)
    servidor.starttls(context=contexto)
    servidor.login(remetente, senha)

    # Construção do email
    mensagem = f"Subject: {assunto}\n\n{mensagem}"
    mensagem = mensagem.encode('utf-8')  # Codifica a mensagem usando UTF-8

    # Envio do email
    servidor.sendmail(remetente, destinatario, mensagem)
    servidor.quit()



if __name__ == "__main__":
    app.run(port=7777)
