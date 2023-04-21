# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getUserInfo')
def user():
    return {
        "code": "200",
        "msg": '获取成功',
        "name": '肖佳明',
        "age": 32
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5344")
