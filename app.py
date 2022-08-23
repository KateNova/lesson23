import os

from flask import Flask, request

from utils import limit, unique, xfilter, lines, sort, xmap

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CMD_DICT = {
    'filter': xfilter,
    'map': xmap,
    'unique': unique,
    'sort': sort,
    'limit': limit
}


@app.route("/perform_query", methods=['POST'])
def perform_query():

    cmd1 = request.args.get('cmd1')
    value1 = request.args.get('value1')
    cmd2 = request.args.get('cmd2')
    value2 = request.args.get('value2')
    file_name = request.args.get('file_name')

    path = f'{DATA_DIR}/{file_name}'

    if not os.path.exists(path):
        return '', 400

    if cmd1 is not None and value1 is not None:
        if cmd1 in CMD_DICT:
            res = lines(path)
            res = list(CMD_DICT[cmd1](res, value1))
        else:
            return '', 400
    else:
        return '', 400

    if cmd2 is not None and value2 is not None:
        if cmd2 in CMD_DICT:
            res = list(CMD_DICT[cmd2](res, value2))
        else:
            return '', 400

    res_str = '\n'.join(res)

    return app.response_class(res_str, content_type="text/plain")


app.run()
