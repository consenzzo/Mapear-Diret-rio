## Mapear-Diretório

**Mapear-Diretório** é um projeto que fornece uma ferramenta simples e eficaz para mapear e listar a estrutura de diretórios e arquivos de um sistema de arquivos. Esta ferramenta é especialmente útil para desenvolvedores e administradores de sistemas que precisam visualizar a hierarquia de diretórios de maneira clara e organizada.

### Funcionalidades

- **Listagem Hierárquica:** Exibe a estrutura de diretórios e arquivos em um formato hierárquico, facilitando a visualização da organização do projeto.
- **Exclusão de Pastas:** Permite a exclusão de pastas específicas da listagem, como `venv`, `__pycache__`, `.git`, entre outras, para focar apenas nos arquivos e diretórios relevantes.
- **Personalização:** Fácil de personalizar para incluir ou excluir quaisquer pastas ou arquivos conforme necessário.

### Estrutura de Diretórios

A estrutura do diretório do projeto é a seguinte:

project_name
|-- module_one
| |-- submodule
| | |-- file_one.py
| | |-- file_two.py
| |
| |-- templates
| |-- module_one
| | |-- template_one.html
| | |-- template_two.html
| | |-- template_three.html
| | |-- template_four.html
| |
| |-- shared_templates
| |-- shared_template.html
|
|-- project_name
| |-- init.py
| |-- settings.py
| |-- urls.py
| |-- wsgi.py
|
|-- main_script.py