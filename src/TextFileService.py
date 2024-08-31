

class TextFileService:

    @classmethod
    def is_file_empty(cls, file_path: str) -> str:
        file_path = f'files/{file_path}.txt'
        try:
            with open(file_path, 'r') as f:
                return 'empty' if not f.read() else 'not empty'
        except FileNotFoundError:
            return 'empty'

    @classmethod
    def read_row_x(cls, file_path: str, row_number: int) -> str:
        file_path = f'files/{file_path}.txt'
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                if row_number < 1 or row_number > len(lines):
                    raise Exception('Invalid row number')
                return lines[row_number - 1].strip()
        except FileNotFoundError:
            raise FileNotFoundError('File not found')

    @classmethod
    def longest_word(cls, file_path: str) -> str:
        file_path = f'files/{file_path}.txt'
        try:
            with open(file_path, 'r') as f:
                words = f.read().split()
                return max(words, key=len)
        except FileNotFoundError:
            raise FileNotFoundError('File not found')

    @classmethod
    def words_frequency(cls, file_path: str) -> dict[str, int]:
        file_path = f'files/{file_path}.txt'
        try:
            with open(file_path, 'r') as f:
                words = f.read().split()
                frequency = {}
                for word in words:
                    frequency[word] = frequency.get(word, 0) + 1
                return frequency
        except FileNotFoundError:
            raise FileNotFoundError('File not found')
