from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route("/hello/<username>")
def hellopage(username):
    return 'Hello %s!' % username


@app.route('/indexserver/<deftwoname>')
def index(deftwoname):
    # print os.system('pwd')
    return render_template('index.html', var_one_value='hello', var_two_value=deftwoname)


@app.route('/showUserName/<showname>')
def show_user_name(showname):
    index(' world')


@app.route('/search_table')
def search_table():
    return index('world')


if __name__ == "__main__":
    app.run(port=8080)
