def read_file (filename: str) -> str:
    with open (filename, 'r') as file:
        return file.read()