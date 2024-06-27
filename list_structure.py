import os

def list_directory(path, level=0, exclude=[]):
    indent = '    ' * level
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        items = []
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path) and item not in exclude:
            print(f"{indent}|--{item}")
            list_directory(item_path, level + 1, exclude)
        elif os.path.isfile(item_path):
            print(f"{indent}|--{item}")

# DIRETÓRIO QUE SERÁ MAPEADO
directory_path = r"ADICIONAR_CAMINHO"

# NOMES DE ARQUIVOS OU PASTAS QUE NÃO DEVEM APARECER NO MAPEAMENTO
exclude_folders = ["venv", "__pycache__", ".git"]


list_directory(directory_path, exclude=exclude_folders)