# Базовый класс для всех файлов
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"Файл: {self.name}, размер: {self.size} bytes"


# Класс для файлов с разрешением на чтение
class ReadableFile(File):
    def __init__(self, name, size, read_permission=True):
        super().__init__(name, size)
        self.read_permission = read_permission

    def __str__(self):
        return f"Файл: {self.name}, размер: {self.size} bytes, чтение: {self.read_permission}"


# Класс для файлов с разрешением на запись
class WritableFile(File):
    def __init__(self, name, size, write_permission=True):
        super().__init__(name, size)
        self.write_permission = write_permission

    def __str__(self):
        return f"Файл: {self.name}, размер: {self.size} bytes, запись: {self.write_permission}"


# Класс для файлов с разрешением на чтение и запись
class ReadWriteFile(ReadableFile, WritableFile):
    def __init__(self, name, size, read_permission=True, write_permission=True):
        # Вызов конструкторов родительских классов
        super().__init__(name, size, read_permission)
        self.write_permission = write_permission

    def __str__(self):
        return f"Файл: {self.name}, размер: {self.size} bytes, чтение: {self.read_permission}, запись: {self.write_permission}"


# Пример использования классов
file1 = File("index.html", 1024)
print(file1)

readable_file = ReadableFile("document.doc", 512)
print(readable_file)

writable_file = WritableFile("program.exe", 2048)
print(writable_file)

read_write_file = ReadWriteFile("data.txt", 4096)
print(read_write_file)