from flask import Flask, render_template, request, send_file, redirect#, abortr
import mysql.connector

mydb = mysql.connector.connect( 
    host = "localhost", 
    user = "root", 
    password = "password", 
    database = "bookLib",
    auth_plugin='mysql_native_password'
    )

app = Flask(__name__, template_folder='templates', static_folder='css')


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
def displayData():
    try: 
        mycursor = mydb.cursor() 
        mycursor.execute("SELECT * FROM bookLib.books;") 
        dbhtml = mycursor.fetchone() 
        # print(dbhtml[1])
        print(repr(dbhtml))
        # return "char"
        # app.logger.warning(dbhtml)
        # app.logger.error(dbhtml)
        # app.logger.info(dbhtml)
        return render_template("search.html", dbhtml =dbhtml)                                   
    except Exception as e: 
        return(str(e))

@app.route('/search.html', methods=['GET'])
def search():
    try: 
        mycursor = mydb.cursor() 
        mycursor.execute("SELECT ElectronicISBN, BookTitle, Author FROM books LIMIT 10;") 
        db = mycursor.fetchall() 
        return render_template("search.html", dbhtml = db)                                   
    except Exception as e: 
        return(str(e))

# @app.route('/', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, host="localhost")