"""
Flask 的模板文件
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'qiku'
    age = 5
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host="192.168.11.11", port="0987", debug=True)
