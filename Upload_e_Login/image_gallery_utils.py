import os


def get_image_gallery():
    files = [
        f for f in os.listdir('static/uploads/')
        if os.path.isfile(os.path.join('static/uploads/', f))
        and os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg', '.png']
    ]
    
    gallery = ''
    for f in files:
        url = f'static/uploads/{f}'
        filename, ext = os.path.splitext(f)
        gallery += f'<div class="image-item">'
        gallery += f'<a href="{url}" target="_blank"><img src="{url}" alt="{filename}" width="200"></a>'
        gallery += f'<p>{filename}</p>'
        gallery += f'</div>'
    
    if gallery:
        gallery = '<hr><h2>Galeria de Imagens</h2>' + gallery
    return gallery
