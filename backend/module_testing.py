

def compress_and_encode(file_path):
    minified_code = minify_python_code(file_path)
    compressed_data = gzip.compress(minified_code.encode('utf-8'))
    encoded_data = base64.b64encode(compressed_data)
    return encoded_data.decode('utf-8')

def decode_and_decompress(encoded_string, output_file_path):
    compressed_data = base64.b64decode(encoded_string)
    decompressed_data = gzip.decompress(compressed_data)
    with open(output_file_path, 'w', newline='') as file:
        file.write(decompressed_data.decode('utf-8'))

def main():
    file_path = '/Users/rama2r/openagi-beta/backend/module.py'
    compressed_string = compress_and_encode(file_path)
    print("Compressed String:", compressed_string)
    
    output_file_path = '/Users/rama2r/openagi-beta/backend/module1.py'
    decode_and_decompress(compressed_string, output_file_path)

if __name__ == '__main__':
    main()