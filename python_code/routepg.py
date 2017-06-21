# coding=utf-8
from flask import Flask
from flask import render_template
from flask import request, jsonify
import os
from format_json.tools import *

app = Flask(__name__)


@app.route("/hello/<username>")
def hellopage(username):
    return 'Hello %s!' % username


# @app.route('/indexserver/<deftwoname>')
# def index(deftwoname):
#     print os.system('pwd')
# return render_template('index.html', var_one_value='hello', var_two_value=deftwoname)


@app.route('/showUserName/<showname>')
def show_user_name(showname):
    index(' world')


# 查询数据库
@app.route('/search_table')
def search_table():
    return render_template('search_sqlite/index.html')


@app.route('/jstest', methods=['POST'])
def hello_page():
    inputname = request.form.get('inputname')
    return jsonify(inputname=('welcome%s' % inputname))


@app.route('/jstestindex/<urlpath>')
def jstest_index(urlpath):
    return render_template('jstest.html', urlpath=urlpath)


@app.route('/requesturl/<urlpath>')
def requesturl_index(urlpath='', params=''):
    return render_template('requesturl/index.html', urlpath=urlpath, params=params)


@app.route('/requesturl')
def requesturl_noparam():
    return requesturl_index('', '')


@app.route('/requesturl_result', methods=['POST'])
def requesturl_result():
    url = request.form.get('url')
    method = request.form.get('method')
    params = request.form.get('params')
    get_test(url, method=method, params=params)
    return requesturl_index(url, str(params))


# 生成周报
@app.route('/weekly')
def build_weekly():
    return ''


@app.route('/index')
def homepage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='172.16.23.5', port=8080)
