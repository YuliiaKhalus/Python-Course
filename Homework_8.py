import os

class AOpen:
    def __init__(self, name, mode, encoding='utf-8'):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.curr = 0
        self.closed = False
        if self.mode == 'r':
            self.fd = os.open(self.name, os.O_RDONLY)
        elif self.mode == 'w':
            self.fd = os.open(self.name, os.O_WRONLY | os.O_CREAT)
        elif self.mode == 'a':
            self.fd = os.open(self.name, os.O_APPEND | os.O_WRONLY | os.O_CREAT)
        elif self.mode == 'rw':
            self.fd = os.open(self.name, os.O_RDWR | os.O_CREAT)
        elif self.mode == 'wr':
            self.fd = os.open(self.name, os.O_RDWR | os.O_CREAT)
        elif self.mode == 'ra':
            self.fd = os.open(self.name, os.O_RDWR | os.O_APPEND)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def isreadable(self):
        if 'r' in self.mode:
            return True
        else:
            return False

    def iswritable(self):
        if self.mode != 'r':
            return True
        else:
            return False

    def read(self, *n):
        if self.isreadable():
            if len(n) == 0:
                content = []
                num = 1
                while True:
                    file_text = os.read(self.fd, num)
                    content.append(file_text.decode())
                    if len(file_text.decode()) < num:
                        break

                self.curr += len(''.join(content))

                return ''.join(content)
            else:
                num = n[0]
                file_text = os.read(self.fd, num)

                self.curr += len(file_text.decode())

                return file_text.decode()

    def readlines(self):
        if self.isreadable():
            file_text = self.read()
            lines = file_text.split('\n')
            return lines

    def readline(self, *n):
        if self.isreadable():
            if len(n) == 0:
                content = []
                num = 1
                while True:
                    file_text = os.read(self.fd, num)
                    content.append(file_text.decode())
                    if file_text.decode() == '\n':
                        break

                self.curr += len(''.join(content))
                return ''.join(content)
            else:
                num = n[0]
                file_text = os.read(self.fd, num)

                self.curr += len(file_text.decode())
                return file_text.decode()

    def write(self, s):
        if self.iswritable():
            s_bytes = str.encode(s)

            self.curr += os.write(self.fd, s_bytes)
            return os.write(self.fd, s_bytes)

    def writeline(self, s):
        if self.iswritable():
            new_line_s = '\n' + s
            s_bytes = str.encode(new_line_s)

            self.curr += os.write(self.fd, s_bytes)
            return os.write(self.fd, s_bytes)

    def writelines(self, lines):
        if self.iswritable():
            for line in lines:
                line_bytes = str.encode(line + '\n')
                os.write(self.fd, line_bytes)
                self.curr += os.write(self.fd, line_bytes)

    def seek(self, pos, how):
        self.curr = pos
        return os.lseek(self.fd, pos, how)

    def tell(self):
        return self.curr

    def close(self):
        self.closed = True
        return os.close(self.fd)


