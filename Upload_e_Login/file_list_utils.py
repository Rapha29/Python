import os

def get_file_list():
    files = [
        f for f in os.listdir('./static/uploads')
        if os.path.isfile(os.path.join('./static/uploads', f))
    ]
    file_groups = {}
    
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext.lower() in ['.pdf', '.txt', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']:
            file_type = 'Documentos'
        elif ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff']:
            file_type = 'Imagens'
        elif ext.lower() in ['.mp3', '.wav', '.wma']:
            file_type = 'Áudio'
        elif ext.lower() in ['.mp4', '.avi', '.mpg', '.mpeg', '.mov', '.wmv']:
            file_type = 'Vídeos'
        elif ext.lower() == '.exe':
            file_type = 'Executável'
        elif ext.lower() == '.zip':
            file_type = 'ZIP'
        elif ext.lower() == '.iso':
            file_type = 'ISO'
        else:
            file_type = 'Outros'

        file_groups.setdefault(file_type, []).append({'url': f'/static/uploads/{f}', 'filename': os.path.basename(f)})
    
    return file_groups
