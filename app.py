from flask import Flask, Response, request

from src.TextFileService import TextFileService

app = Flask(__name__)


@app.route('/content')
def content() -> Response:  # put application's code here
    try:
        with open('files/names.txt', 'r') as f:
            names = f.read()
            return Response(names, status=200)
    except FileNotFoundError:
        return Response(status=404)


# adds word hello to names file
@app.route('/register')
def register() -> Response:
    try:
        with open('files/names.txt', 'a') as f:
            f.write('\nhello\n')
            return Response('success', status=200)
    except FileNotFoundError:
        return Response(status=404)


@app.route('/empty')
def empty() -> str:
    file_name = request.args.get('file_name')
    return TextFileService.is_file_empty(file_name)


@app.route('/row_content')
def row_content() -> str:
    file_name = request.args.get('file_name')
    row_number = int(request.args.get('row_number'))
    return TextFileService.read_row_x(file_name, row_number)


@app.route('/longest')
def longest_word() -> str:
    file_name = request.args.get('file_name')
    return TextFileService.longest_word(file_name)


@app.route('/frequency')
def words_frequency() -> dict[str, int]:
    file_name = request.args.get('file_name')
    return TextFileService.words_frequency(file_name)


if __name__ == '__main__':
    app.run()
