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

# @app.route('/search.html', methods=['GET'])
# def searchPage():
#     cur = con.cursor()
#     cur.execute("SELECT * FROM bookLib.books")
#     data = cur.fetchall()
#     return render_template('search.html', data=data)

# @app.route('/search.html', methods=['GET'])
# def displayData():
#     try: 
#         mycursor = mydb.cursor() 
#         mycursor.execute("SELECT * FROM bookLib.books;") 
#         dbhtml = mycursor.fetchone() 
#         # print(dbhtml[1])
#         # print(repr(dbhtml))
#         # return "char"
#         # app.logger.warning(dbhtml)
#         # app.logger.error(dbhtml)
#         # app.logger.info(dbhtml)
#         return render_template("search.html", dbhtml =dbhtml)                                   
#     except Exception as e: 
#         return(str(e))

@app.route('/search.html', methods=['GET'])
def search():
    try: 
        mycursor = mydb.cursor() 
        mycursor.execute("SELECT ElectronicISBN, BookTitle, Author FROM books;") 
        dbhtml = mycursor.fetchall() 
        return render_template("search.html", dbhtml = dbhtml)                                   
    except Exception as e: 
        return(str(e))

@app.route('/search.html?q=<column>+<searchTerm>', methods=['GET'])
def searchTerm(column,searchTerm):
    try: 
    #     column = column
    #     searchTerm = searchTerm
        # if column == "all":
        #     column = "ElectronicISBN like" +searchTerm "or BookTitle like" +searchTerm "or Author"
        mycursor = mydb.cursor() 
        mycursor.execute("SELECT ElectronicISBN, BookTitle, Author FROM books WHERE %s like %s;", (column,searchTerm)) 
        dbhtml = mycursor.fetchall() 
        # print(repr(dbhtml))
        return render_template("search.html", dbhtml = dbhtml)                                   
    except Exception as e: 
        return(str(e))

# @app.route('/', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, host="localhost")