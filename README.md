## Estrutura de Diretórios

Exemplo de mapeamento realizado pelo script:

project_name
|--module_one
|   |--submodule
|   |   |--file_one.py
|   |   |--file_two.py
|   |
|   |--templates
|       |--module_one
|       |   |--template_one.html
|       |   |--template_two.html
|       |   |--template_three.html
|       |   |--template_four.html
|       |
|       |--shared_templates
|           |--shared_template.html
|
|--project_name
|   |--__init__.py
|   |--settings.py
|   |--urls.py
|   |--wsgi.py
|
|--main_script.py

Pastas específicas como `venv`, `__pycache__`, `.git`, etc., podem ser ignoradas para simplificar a visualização.