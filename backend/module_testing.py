





def main():
    file_path = '/Users/rama2r/openagi-beta/backend/module.py'
    compressed_string = compress_and_encode(file_path)
    print("Compressed String:", compressed_string)
    
    output_file_path = '/Users/rama2r/openagi-beta/backend/module1.py'
    decode_and_decompress(compressed_string, output_file_path)

if __name__ == '__main__':
    main()