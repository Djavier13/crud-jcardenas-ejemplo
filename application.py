from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'hola mundooo'

if __name__ == '__main__':
  app.run(port=80, debug=False)
