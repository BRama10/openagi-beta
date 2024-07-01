import os
import yaml
import ast
import requests
import json
from pprint import pprint
def load_config(path: str) -> None:
    base_name = os.path.splitext(os.path.basename(path))[0]
    py_file_path = f"{base_name}.py"
    with open(path, 'r') as file:
        yaml_content = yaml.safe_load(file)
    meta = yaml_content.get('meta', {})
    author = meta.get('author')
    version = meta.get('version')
    name = meta.get('name')
    py_content = ""
    if author:
        py_content += f"AUTHOR = '{author}'\n"
    if version is not None:  # version can be 0
        py_content += f"VERSION = {version}\n"
    if name:
        py_content += f"NAME = '{name}'\n"
    py_content += "\n"  # Add a blank line for readability
    lines = yaml_content.get('lines', [])
    for line_data in lines:
        indent = line_data['indent']
        line = line_data['line']
        py_content += " " * indent + line + "\n"
    with open(py_file_path, 'w') as file:
        file.write(py_content)
    print(f"Created {py_file_path} from {path}")
def upload_agent(path: str) -> tuple[str, float]:
    with open(path, 'r') as file:
        yaml_content = yaml.safe_load(file)
    headers = {
        "Content-Type": "application/json",
    }
    upload_content = {
        'name' : yaml_content.get('meta').get('name'),
        'author' : yaml_content.get('meta').get('author'),
        'version' : float(yaml_content.get('meta').get('version')),
        'file_data': yaml_content.get('lines')
    }
    url = 'http://localhost:3000/api/upload'
    pprint(upload_content)
    response = requests.post(url,
                             data=json.dumps(upload_content),
                             headers=headers,
                             )
    print(response.data)
def download_agent(name: str, version: float | None) -> None:
    if version:
        query = f'https://localhost:3000/api/download?version={version}&name={name}'
    else:
        query = f'http://localhost:3000/api/download?name={name}'
    response = requests.get(query)
    print(response.json())
def write_config(path: str) -> None:
    base_name = os.path.splitext(os.path.basename(path))[0]
    yaml_file_path = f"{base_name}.yaml"
    with open(path, 'r') as file:
        py_content = file.read()
    tree = ast.parse(py_content)
    author, version, name = None, None, None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if node.targets[0].id == 'AUTHOR':
                author = node.value.s
            elif node.targets[0].id == 'VERSION':
                version = node.value.n
            elif node.targets[0].id == 'NAME':
                name = node.value.s
    lines = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            lines.append({"line": f"def {node.name}():", "indent": 0})
            for sub_node in node.body:
                if isinstance(sub_node, (ast.Assign, ast.Return)):
                    code_line = ast.unparse(sub_node).strip()
                    lines.append({"line": code_line, "indent": 4})
    yaml_content = {
        "meta": {
            "author": author,
            "version": version,
            "name": name
        },
        "lines": lines
    }
    with open(yaml_file_path, 'w') as file:
        yaml.dump(yaml_content, file, default_flow_style=False)
    print(f"Created {yaml_file_path} from {path}")
download_agent('Example Agent 2', version=None)