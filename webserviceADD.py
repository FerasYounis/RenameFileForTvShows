from flask import Flask
from flask import request
from pip._vendor.requests.packages.urllib3.packages.six import int2byte

app = Flask(__name__)

@app.route('/')
def Add():
    num1 = request.args.get('num1',type=int)
    num2 = request.args.get('num2',type=int)

    result = num1 + num2
    return str(result)


if __name__ == '__main__':
    app.run()