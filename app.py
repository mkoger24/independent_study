from flask import Flask, render_template, request, send_file, redirect#, abortr
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static',static_url_path='/static')


@app.route('/source/SpringerNatureBooks.csv')
def serve_source(filename):
    return send_from_directory('source', SpringerNatureBooks)

@app.route('/', methods=['GET'])
def index():
    return render_template("home.html")

@app.route('/home.html', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/login.html', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/bookInfo.html', methods=['GET'])
def bookInfo():
    return render_template("bookInfo.html")

@app.route('/search.html', methods=['GET'])
def search():
    return render_template("search.html")

@app.route('/test.html', methods=['GET'])
def test():
    return render_template("test.html")

# @app.route('/', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, host="localhost")