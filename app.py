# -*- coding: utf-8 -*-

import sys
import time
import json

import pandas as pd
from flask import Flask
from flask.ext.restful import Api, Resource
from flask import Flask, request, send_file, Response, render_template



app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.secret_key = 'ok, do u l0ve me ~^_ '
api = Api(app)


def get_line_data():
    _dict = json.load(file('logs/latest.json', 'r'))
    df = pd.DataFrame.from_dict(_dict)

    return df


class Main(Resource):
    def get(self): 
        df = get_line_data()

        return Response(render_template('display.html'))


api.add_resource(Main, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
