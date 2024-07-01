import gzip
import base64

class Interact:
    def __init__(self, file_path: None):
        self.file_path = file_path
        self.minified_code: str | None =  None

    def load()

    def minify_python_code(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
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
    
    def decode_and_decompress(self):
        compressed_data = base64.b64decode(self.encoded_string)
        decompressed_data = gzip.decompress(compressed_data)
        
        with open(self.output_file_path, 'w', newline='') as file:
            file.write(decompressed_data.decode('utf-8'))
        
        return self