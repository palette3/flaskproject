from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "欢迎来到Flask首页"


@app.route("/<int:pk>")
def detail(pk):
    return f"欢迎来到Flask首页{pk}"


if __name__ == '__main__':
    # debug=Ture 可以启动热更新 代码发生变化 不用启动服务器
    app.run(host="192.168.11.11", port="0987", debug=True)