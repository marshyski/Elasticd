from flask import Flask
from registrar import Registrar

app = Flask(__name__.split('.')[0])

_registrar = None

def set_registrar(registrar):
    global _registrar
    _registrar = registrar


@app.route('/')
def home():
    return 'welcome'


@app.route('/register')
def register():
    _registrar.register()
    return 'registered'


@app.route('/deregister')
def deregister():
    _registrar.deregister()
    return 'deregestered'


def start():
    app.run()


if __name__ == '__main__':
    start()
