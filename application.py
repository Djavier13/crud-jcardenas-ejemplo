import os
from flask import Flask, render_template
app = Flask(__name__)

nombre = os.environ['nombre']
@app.route('/')
def index():
    return 'hola mundooo desde mi maquina'

if __name__ == '__main__':
  app.run(port=80, debug=False)
