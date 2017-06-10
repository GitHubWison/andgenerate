from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route("/hello/<username>")
def hellopage(username):
    return 'Hello %s!' % username


@app.route('/index/<loginname>')
def index(loginname):
    # print os.system('pwd')
    return render_template('test.html', name=loginname)


@app.route('/showUserName/<showname>')
def show_user_name(showname):
    return showname


if __name__ == "__main__":
    app.run()
