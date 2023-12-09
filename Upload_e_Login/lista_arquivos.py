import os

def agrupar_arquivos(pasta):
    tipos_arquivos = {
        'av': 'Avaliações Virtuais',
        'ta': 'Tele Aulas',
        'cw': 'Conteúdo Web',
        'livro': 'Livros',
        'prova': 'Provas',
        'portfolios': 'Portfólios',
        'resumos': 'Resumos'
    }
    
    def determinar_tipo_arquivo(filename):
        filename_lower = filename.lower()
        for chave, tipo in tipos_arquivos.items():
            if chave in filename_lower:
                return tipo
        return 'Outros'

    files = [
        f for f in os.listdir(f'./static/uploads/{pasta}')
        if os.path.isfile(os.path.join(f'./static/uploads/{pasta}', f)) and f.lower().endswith('.pdf')
    ]
    file_groups = {}
    
    for f in files:
        file_type = determinar_tipo_arquivo(f)
        file_groups.setdefault(file_type, []).append({'url': f'/static/uploads/{pasta}/{f}', 'filename': f})    
    return file_groups

def arquitetura():
    return agrupar_arquivos('arquitetura')

def redes_de_computadores():
    return agrupar_arquivos('redes_de_computadores')

def projeto_de_software():
    return agrupar_arquivos('projeto_de_software')

def sociedade_fazueli():
    return agrupar_arquivos('sociedade_fazueli')

def seguranca_e_auditoria():
    return agrupar_arquivos('seguranca_e_auditoria')

def logica_e_matematica_computacional():
    return agrupar_arquivos('logica_e_matematica_computacional')

def linguagem_de_programacao():
    return agrupar_arquivos('linguagem_de_programacao')

def engenharia_de_software():
    return agrupar_arquivos('engenharia_de_software')

def analise_e_modelagem():
    return agrupar_arquivos('analise_e_modelagem')

def algoritmos_e_programacao():
    return agrupar_arquivos('algoritmos_e_programacao')

def analise_orientada_objetos():
    return agrupar_arquivos('analise_orientada_objetos')

def sistemas_operacionais():
    return agrupar_arquivos('sistemas_operacionais')

def modelagem_de_dados():
    return agrupar_arquivos('modelagem_de_dados')

def prog_e_desen_bd():
    return agrupar_arquivos('prog_e_desen_bd')

def projeto_de_extensao():
    return agrupar_arquivos('projeto_de_extensao')


