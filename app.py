from flask import Flask

# 初始化 Flask 應用
app = Flask(__name__)

# 定義首頁路由
@app.route('/')
def hello_world():
    return '吳承諺'

# 啟動應用
if __name__ == '__main__':
    app.run(debug=True)
