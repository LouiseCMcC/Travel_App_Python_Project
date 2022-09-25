from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(destinations_blueprint)

if __name__ = '__main__':
    app.run(debug=True)

