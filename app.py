from flask import Flask, render_template, request, send_file, redirect, request#, abortr
import mysql.connector

mydb = mysql.connector.connect( 
    host = "localhost", 
    user = "root", 
    password = "password", 
    database = "bookLib",
    auth_plugin='mysql_native_password'
    )

app = Flask(__name__, template_folder='templates', static_folder='static')


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

# @app.route('/search.html', methods=['GET'])
# def search():
#     # return "word"
#     try: 
#         mycursor = mydb.cursor() 
#         mycursor.execute("SELECT ElectronicISBN, BookTitle, Author FROM books;") 
#         dbhtml = mycursor.fetchall() 
#         return render_template("search.html", dbhtml = dbhtml)                                   
#     except Exception as e: 
#         return(str(e))

@app.route('/search.html', methods=['GET'])
def searchTerm():
    # get all arguments from url
    arguments = request.args.get("q")

    try: 
        # if there are arguments, store them in column and searchTerm
        if arguments:
            search = arguments.split('.')
            print(search)
            column = search[0]
            searchTerm = search[1]
            print(column)
            print(searchTerm)
        
        # if there are no specified search parameters, display all entries
        else:
            query = "SELECT ElectronicISBN, BookTitle, Author FROM books;"
            mycursor = mydb.cursor() 
            mycursor.execute(query) 
            dbhtml = mycursor.fetchall() 
            return render_template("search.html", dbhtml = dbhtml)

        # TODO add popup here, or just display all entries?
        # TODO logical operation needs changed
        if searchTerm == None:
            return "must enter a search term"

        # specifying a query to use based on the intended column to search
        elif column == 'BookTitle':
            query = "SELECT ElectronicISBN, BookTitle, Author FROM books WHERE BookTitle like '%" + searchTerm + "%';"

        elif column == 'ElectronicISBN':
            query = "SELECT ElectronicISBN, BookTitle, Author FROM books WHERE ElectronicISBN like '%" + searchTerm + "%';"

        elif column == 'Author':
            query = "SELECT ElectronicISBN, BookTitle, Author FROM books WHERE Author like '%" + searchTerm + "%';"

        # if all columns is specified
        # TODO test this functionality
        elif column == 'All':
            query = "SELECT ElectronicISBN, BookTitle, Author FROM books WHERE BookTitle like'%" + searchTerm + "%' or WHERE ElectronicISBN like'%" + searchTerm + "%' or WHERE Author like '%" + searchTerm + "%';"

        # run the query and return the template
        mycursor = mydb.cursor() 
        mycursor.execute(query) 
        dbhtml = mycursor.fetchall() 
        return render_template("search.html", dbhtml = dbhtml)

        
    except Exception as e: 
        return(str(e))

# @app.route('/', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, host="localhost")