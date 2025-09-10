import os
from tkinter.filedialog import askdirectory

path = askdirectory(title='Selecione a pasta com os arquivos que deseja organizar')
lista_arquivos = os.listdir(path)
locais = {'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
          'Documentos': ['.pdf', '.doc', '.docx', '.txt'],
          'Planilhas': ['.xls', '.xlsx', '.csv'],
          'Apresentações': ['.ppt', '.pptx'],
          'Arquivos compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
          'Vídeos': ['.mp4', '.avi', '.mov', '.mkv'],
          'Áudios': ['.mp3', '.wav', '.aac', '.flac'],
          'Scripts': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp'],
          'Outros': []}

for arquivo in lista_arquivos:
    nome, ext = os.path.splitext(f'{path}/{arquivo}')
    for pasta in locais:
        if ext.lower() in locais[pasta]:
            if not os.path.exists(f'{path}/{pasta}'):
                os.makedirs(f'{path}/{pasta}')
            os.rename(f'{path}/{arquivo}', f'{path}/{pasta}/{arquivo}')
            break
   