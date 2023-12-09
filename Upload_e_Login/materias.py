import os
from flask import Flask, request, send_from_directory, render_template, jsonify, g, redirect
from lista_arquivos import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def render_arquitetura():
    file_list = arquitetura()
    return render_template('arquitetura.html', file_list=file_list)

@app.route('/projeto_de_software', methods=['GET'])
def render_projeto_de_software():
    file_list = projeto_de_software()
    return render_template('projeto_de_software.html', file_list=file_list)

@app.route('/sociedade_fazueli', methods=['GET'])
def render_sociedade_fazueli():
    file_list = sociedade_fazueli()
    return render_template('sociedade_fazueli.html', file_list=file_list)

@app.route('/interface_e_usabilidade', methods=['GET'])
def render_interface_e_usabilidade():
    file_list = interface_e_usabilidade()
    return render_template('arquitetura.html', file_list=file_list)

@app.route('/seguranca_e_auditoria', methods=['GET'])
def render_seguranca_e_auditoria():
    file_list = seguranca_e_auditoria()
    return render_template('seguranca_e_auditoria.html', file_list=file_list)

@app.route('/logica_e_matematica_computacional', methods=['GET'])
def render_logica_e_matematica_computacional():
    file_list = logica_e_matematica_computacional()
    return render_template('logica_e_matematica_computacional.html', file_list=file_list)

@app.route('/linguagem_de_programacao', methods=['GET'])
def render_linguagem_de_programacao():
    file_list = linguagem_de_programacao()
    return render_template('linguagem_de_programacao.html', file_list=file_list)

@app.route('/engenharia_de_software', methods=['GET'])
def render_engenharia_de_software():
    file_list = engenharia_de_software()
    return render_template('engenharia_de_software.html', file_list=file_list)

@app.route('/algoritmos_e_programacao', methods=['GET'])
def render_algoritmos_e_programacao():
    file_list = algoritmos_e_programacao()
    return render_template('algoritmos_e_programacao.html', file_list=file_list)

@app.route('/analise_orientada_objetos', methods=['GET'])
def render_analise_orientada_objetos():
    file_list = analise_orientada_objetos()
    return render_template('analise_orientada_objetos.html', file_list=file_list)

@app.route('/sistemas_operacionais', methods=['GET'])
def render_sistemas_operacionais():
    file_list = sistemas_operacionais()
    return render_template('sistemas_operacionais.html', file_list=file_list)

@app.route('/modelagem_de_dados', methods=['GET'])
def render_modelagem_de_dados():
    file_list = modelagem_de_dados()
    return render_template('modelagem_de_dados.html', file_list=file_list)

@app.route('/prog_e_desen_bd', methods=['GET'])
def render_prog_e_desen_bd():
    file_list = prog_e_desen_bd()
    return render_template('prog_e_desen_bd.html', file_list=file_list)

@app.route('/projeto_de_extensao', methods=['GET'])
def render_projeto_de_extensao():
    file_list = projeto_de_extensao()
    return render_template('projeto_de_extensao.html', file_list=file_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
