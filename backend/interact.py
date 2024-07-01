import gzip
import base64

class Interact:
    def __init__(self, file_path: None):
        self.file_path = file_path
        self.minified_code: str | None =  None

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
    
    def