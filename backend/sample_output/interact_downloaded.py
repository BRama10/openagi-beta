import gzip
import base64
import subprocess
import sys
import json
import pprint
import requests
class Interact:
    def __init__(self, file_path: str | None = None, name: str = '', config: str = 'config.json'):
        self.file_path = file_path
        self.minified_code: str | None = None
        self.encoded_string: str | None = None
        self.output_file_path: str | None = None
        self.reqs: str | None = None
        self.compressed_reqs: str | None = None
        self.name = name
        self.config = config
    def minify_python_code(self):
        with open(self.file_path, 'r') as file:
            lines: list[str] = file.readlines()
        minified_lines = []
        for line in lines:
            stripped_line = line.rstrip()
            if stripped_line and not stripped_line.lstrip().startswith("#"):
                minified_lines.append(stripped_line)
        self.minified_code = "\n".join(minified_lines)
        return self
    def compress(self):
        compressed_data = gzip.compress(self.minified_code.encode('utf-8'))
        encoded_data = base64.b64encode(compressed_data)
        self.encoded_data = encoded_data.decode('utf-8')
        return self
    def compress_reqs(self):
        with open(f"meta_{self.name}_reqs.txt", 'r') as file:
            self.reqs: str = file.read()
        cleaned = [line.strip() for line in self.reqs.split(
            '\n') if line.strip() and not line.startswith('#')]
        minified = ';'.join(cleaned)
        compressed = gzip.compress(minified.encode('utf-8'))
        self.compressed_reqs = base64.b64encode(compressed).decode('utf-8')
        return self
    def decompress_reqs(self):
        decompressed = gzip.decompress(base64.b64decode(self.compressed_reqs))
        minified = decompressed.decode('utf-8')
        expanded = minified.replace(';', '\n')
        output_filename = f"meta_{self.name}_reqs.txt"
        with open(output_filename, 'w') as file:
            file.write(expanded)
        return self
    def decompress(self):
        compressed_data = base64.b64decode(self.encoded_string)
        decompressed_data = gzip.decompress(compressed_data)
        with open(self.output_file_path, 'w', newline='') as file:
            file.write(decompressed_data.decode('utf-8'))
        return self
    def get_compressed_data(self):
        return {
            'python': self.encoded_data,
            'reqs': self.compressed_reqs
        }
    def upload(self):
        with open(self.config, 'r') as file:
            data: dict[str, dict] = json.load(file)
        meta = data.get('meta')
        headers = {
            "Content-Type": "application/json",
        }
        upload_content = {
            'name': meta.get('name'),
            'author': meta.get('author'),
            'version': float(meta.get('version')),
            'description': meta.get('description'),
            'license': meta.get('license'),
            'file_data': self.encoded_data,
            'dependencies': self.compressed_reqs
        }
        url = 'https://openagi-beta.vercel.app/api/upload'
        pprint.pprint(upload_content)
        response = requests.post(url,
                                 data=json.dumps(upload_content),
                                 headers=headers,
                                 )
        pprint.pprint(response.content)
        return self
    def download_agent(name: str, version: float | None) :
        if version:
            query = f'https://localhost:3000/api/download?version={version}&name={name}'
        else:
            query = f'http://localhost:3000/api/download?name={name}'
        response = requests.get(query)
        print(response.json())
    def _install(self):
        with open(f"meta_{self.name}_reqs.txt", 'r') as file:
            requirements = file.readlines()
        for requirement in requirements:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", requirement.strip()])
        subprocess.check_call([sys.executable, "-m", "playwright", "install"])
        return self
if __name__ == '__main__':
    client = Interact('interact.py', name='web')
    client.minify_python_code().compress().compress_reqs().upload()