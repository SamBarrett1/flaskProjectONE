from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return 'Hello {}'.format(name)


@app.route('/get_fahrenheit')
@app.route('/get_fahrenheit/<celsius>')
def get_fahrenheit(celsius=''):
    """get fahrenheit from celsius"""
    return "Result: {:.1f} C is {:.2f} F".format(float(celsius), float(celsius) * 9.0 / 5 + 32)


if __name__ == '__main__':
    app.run()
