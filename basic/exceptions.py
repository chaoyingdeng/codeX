class CodeXException(Exception):
    def __str__(self):
        return 'CodeXError'


class BrowserTypeError(CodeXException):
    def __init__(self, browser_type):
        self._type = browser_type

    def __str__(self):
        return f'Unsupported browser type: {self._type}'


class ElementTypeError(CodeXException):
    def __init__(self, ele_type):
        self._type = ele_type

    def __str__(self):
        return f'Element type: {self._type}'


class ElementNotExistsError(CodeXException):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return f'Element is None: {self._value}'


class FileNotExists(CodeXException):
    def __init__(self, file_path):
        self._file_path = file_path

    def __str__(self):
        return f'File Not Exists: {self._file_path}'


class ExcelSheetError(CodeXException):
    def __int__(self, index):
        self._index = index

    def __str__(self):
        return f'Excel not {self._index} Sheet'
