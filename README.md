# 🐍 Projetos em Python

Este repositório contém dois projetos simples e úteis desenvolvidos em **Python**:

1. **Mesclador de PDFs** – une vários arquivos PDF em um único documento.  
2. **Organizador de Arquivos** – organiza automaticamente arquivos em pastas, de acordo com sua extensão.

---

## 🚀 Como usar

Você pode executar os projetos de duas formas:

### 1. Usando os arquivos `.exe` (mais fácil)
Basta baixar os executáveis gerados na pasta `dist/` e rodar normalmente:

- Mesclador de PDFs:
  ```bash
  Mesclador de PDFs.exe
  ```
- Organizador de Arquivos:
  ```bash
  Organizador de Arquivos.exe
  ```

### 2. Executando com Python (recomendado para desenvolvedores)

#### Passo 1 – Clonar o repositório
```bash
git clone https://github.com/PedroCavalcantiFigueiredo/Projetos-Python.git
cd Projetos-Python
```

#### Passo 2 – Criar ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

#### Passo 3 – Instalar dependências
```bash
pip install -r requirements.txt
```

#### Passo 4 – Executar os scripts
- Mesclador de PDFs:
  ```bash
  python Mesclador-de-pdfs/mesclador_pdfs.py
  ```
- Organizador de Arquivos:
  ```bash
  python Organizador-de-arquivos/organizador_arquivos.py
  ```

---

## 📂 1. Mesclador de PDFs

### Descrição
Este script permite selecionar uma pasta com arquivos PDF e mesclá-los em um único documento, preservando a ordem alfabética dos arquivos.

### Tecnologias utilizadas
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [OS](https://docs.python.org/3/library/os.html)

### Saída
O resultado será salvo em:
```
Mesclador-de-pdfs/Arquivo_mesclado.pdf
```

---

## 📂 2. Organizador de Arquivos

### Descrição
Este script organiza automaticamente arquivos de uma pasta em subpastas categorizadas (imagens, documentos, planilhas, vídeos etc.).

### Tecnologias utilizadas
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [OS](https://docs.python.org/3/library/os.html)

### Estrutura final de pastas (exemplo)
```
├── Imagens
├── Documentos
├── Planilhas
├── Vídeos
├── Áudios
├── Scripts
└── Outros
```

### 💡 Exemplos de categorias
- **Imagens**: `.jpg`, `.png`, `.gif`...  
- **Documentos**: `.pdf`, `.docx`, `.txt`...  
- **Planilhas**: `.xls`, `.csv`...  
- **Vídeos**: `.mp4`, `.avi`...  
- **Áudios**: `.mp3`, `.wav`...  
- **Scripts**: `.py`, `.js`, `.html`...  
- **Outros**: arquivos sem categoria definida.  

---

## ⚡ Requisitos
- Python 3.x  
- Dependências listadas em `requirements.txt`

📌 Observação: Os dois projetos utilizam a biblioteca `tkinter` para abrir uma janela de seleção de pastas, portanto é necessário executar em um ambiente com suporte gráfico.

---

## 👨‍💻 Autor
Desenvolvido por **Pedro Cavalcanti Figueiredo**
