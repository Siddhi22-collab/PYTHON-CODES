class FileOpener:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    
    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileOpener("sample.txt", "w") as f:
    f.write("Hello context manager!")
