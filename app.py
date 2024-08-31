from flask import Flask, Response, send_file

from src import ImageService

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


if __name__ == '__main__':
    app.run()
