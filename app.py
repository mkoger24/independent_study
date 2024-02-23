from flask import Flask, render_template, request, send_file, redirect, request#, abortr
import mysql.connector
import datetime

mydb = mysql.connector.connect( 
    host = "localhost", 
    user = "root", 
    password = "password", 
    database = "bookLib",
    auth_plugin='mysql_native_password'
)

login = False

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def index():
    return render_template("home.html")

@app.route('/home.html', methods=['GET',"POST"])
def home():
    if request.method == "POST":
        column = request.form["searchColumn"]
        searchTerm = request.form['searchTerm']
        print('column: ',column)
        print('searchTerm:', searchTerm)
    
    # if there are no specified search parameters, display all entries
        if column=='':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"
            mycursor = mydb.cursor() 
            mycursor.execute(query) 
            dbhtml = mycursor.fetchall() 
            return render_template("search.html", dbhtml = dbhtml)

        # TODO add popup here, or just display all entries?
        # TODO logical operation needs changed
        if searchTerm == None:
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"
            mycursor = mydb.cursor() 
            mycursor.execute(query) 
            dbhtml = mycursor.fetchall() 
            return render_template("search.html", dbhtml = dbhtml)

        # specifying a query to use based on the intended column to search
        elif column == 'BookTitle':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE BookTitle like '%" + searchTerm + "%';"

        elif column == 'ElectronicISBN':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE ElectronicISBN like '%" + searchTerm + "%';"

        elif column == 'Author':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE Author like '%" + searchTerm + "%';"

        elif column == 'CopyrightYear':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE CopyrightYear like '%" + searchTerm + "%';"

        # if all columns is specified
        # TODO test this functionality
        elif column == 'All':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE BookTitle like'%" + searchTerm + "%' or WHERE ElectronicISBN like'%" + searchTerm + "%' or WHERE Author like '%" + searchTerm + "%';"
        
        else:
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"

        # run the query and return the template
        mycursor = mydb.cursor() 
        mycursor.execute(query) 
        dbhtml = mycursor.fetchall() 
        return render_template("search.html", dbhtml = dbhtml)
    return render_template("home.html")

@app.route('/login.html', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/search.html', methods=['GET','POST'])
def searchTerm():

    try: 
        # get all arguments from url
        arguments = request.args.get("q")

        # if there are arguments, store them in column and searchTerm
        if request.method == "POST":
            column = request.form["searchColumn"]
            searchTerm = request.form['searchTerm']
            print('column: ',column)
            print('searchTerm:', searchTerm)
        
        # if there are no specified search parameters, display all entries
        else:
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"
            mycursor = mydb.cursor() 
            mycursor.execute(query) 
            dbhtml = mycursor.fetchall() 
            return render_template("search.html", dbhtml = dbhtml)

        # TODO add popup here, or just display all entries?
        # TODO logical operation needs changed
        if searchTerm == None:
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"
            mycursor = mydb.cursor() 
            mycursor.execute(query) 
            dbhtml = mycursor.fetchall() 
            return render_template("search.html", dbhtml = dbhtml)

        # specifying a query to use based on the intended column to search
        elif column == 'BookTitle':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE BookTitle like '%" + searchTerm + "%';"

        elif column == 'ElectronicISBN':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE ElectronicISBN like '%" + searchTerm + "%';"

        elif column == 'Author':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE Author like '%" + searchTerm + "%';"

        elif column == 'CopyrightYear':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE CopyrightYear like '%" + searchTerm + "%';"

        # if all columns is specified
        # TODO test this functionality
        elif column == 'All':
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE BookTitle like'%" + searchTerm + "%' or WHERE ElectronicISBN like'%" + searchTerm + "%' or WHERE Author like '%" + searchTerm + "%';"
        
        else:
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"

        # run the query and return the template
        mycursor = mydb.cursor() 
        mycursor.execute(query) 
        dbhtml = mycursor.fetchall() 
        return render_template("search.html", dbhtml = dbhtml)


    except Exception as e: 
        return(str(e))

@app.route('/details.html', methods=['GET','POST'])
def display():

    try:
        if request.method == "POST":
            id = request.args.get("q")
            comment = request.form["userComment"]
            tag = request.form['userTag']

            now = datetime.datetime.now()

            month = str(now.month) 
            day = str(now.day) 
            year = str(now.year)
            hour = str(now.hour)
            minute = now.minute
            if minute < 10:
                minute = "0"+str(minute)
            else:
                minute = str(minute)
            dateTime = month +"-"+ day +"-"+ year +" "+ hour +":"+ minute

            if comment != '' and tag != '':

                query = "INSERT INTO comments (book_id, Comment, DateTime, User) VALUES ('" + id + "', '" + comment +"', '" + dateTime + "', 'testuser');"
                mycursor = mydb.cursor() 
                mycursor.execute(query) 
                bookdb = mycursor.fetchall() 

                query = "INSERT INTO tags () VALUES ('" + id + "', '" + tag +"');"
                mycursor = mydb.cursor() 
                mycursor.execute(query) 
                bookdb = mycursor.fetchall() 

                id = request.args.get("q")
                bookInfoQuery = "SELECT * FROM books WHERE id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(bookInfoQuery) 
                bookdb = mycursor.fetchall() 

                commentQuery = "SELECT * FROM comments WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(commentQuery) 
                commentdb = mycursor.fetchall() 
                
                tagQuery = "SELECT Tag FROM tags WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(tagQuery) 
                tagdb = mycursor.fetchall() 

                return render_template("details.html", bookdb = bookdb, commentdb = commentdb, tagdb = tagdb, id = id)
            elif comment != '' and tag == '':

                query = "INSERT INTO comments (book_id, Comment, DateTime, User) VALUES ('" + id + "', '" + comment +"', '" + dateTime + "', 'testuser');"
                mycursor = mydb.cursor() 
                mycursor.execute(query) 
                bookdb = mycursor.fetchall() 

                id = request.args.get("q")
                bookInfoQuery = "SELECT * FROM books WHERE id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(bookInfoQuery) 
                bookdb = mycursor.fetchall() 

                commentQuery = "SELECT * FROM comments WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(commentQuery) 
                commentdb = mycursor.fetchall() 
                
                tagQuery = "SELECT Tag FROM tags WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(tagQuery) 
                tagdb = mycursor.fetchall() 

                return render_template("details.html", bookdb = bookdb, commentdb = commentdb, tagdb = tagdb, id = id)
            elif comment == '' and tag != '': 

                query = "INSERT INTO tags () VALUES ('" + id + "', '" + tag +"');"
                mycursor = mydb.cursor() 
                mycursor.execute(query) 
                bookdb = mycursor.fetchall() 

                id = request.args.get("q")
                bookInfoQuery = "SELECT * FROM books WHERE id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(bookInfoQuery) 
                bookdb = mycursor.fetchall() 

                commentQuery = "SELECT * FROM comments WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(commentQuery) 
                commentdb = mycursor.fetchall() 
                
                tagQuery = "SELECT Tag FROM tags WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(tagQuery) 
                tagdb = mycursor.fetchall() 

                return render_template("details.html", bookdb = bookdb, commentdb = commentdb, tagdb = tagdb, id = id)
            else:
                id = request.args.get("q")
                bookInfoQuery = "SELECT * FROM books WHERE id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(bookInfoQuery) 
                bookdb = mycursor.fetchall() 

                commentQuery = "SELECT * FROM comments WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(commentQuery) 
                commentdb = mycursor.fetchall() 

                tagQuery = "SELECT Tag FROM tags WHERE book_id = '" + id + "';"
                mycursor = mydb.cursor() 
                mycursor.execute(tagQuery) 
                tagdb = mycursor.fetchall() 

                return render_template("details.html", bookdb = bookdb, commentdb = commentdb, tagdb = tagdb, id = id)
        else:

            id = request.args.get("q")
            bookInfoQuery = "SELECT * FROM books WHERE id = '" + id + "';"
            mycursor = mydb.cursor() 
            mycursor.execute(bookInfoQuery) 
            bookdb = mycursor.fetchall() 

            commentQuery = "SELECT * FROM comments WHERE book_id = '" + id + "';"
            mycursor = mydb.cursor() 
            mycursor.execute(commentQuery) 
            commentdb = mycursor.fetchall() 

            tagQuery = "SELECT Tag FROM tags WHERE book_id = '" + id + "';"
            mycursor = mydb.cursor() 
            mycursor.execute(tagQuery) 
            tagdb = mycursor.fetchall() 

            return render_template("details.html", bookdb = bookdb, commentdb = commentdb, tagdb = tagdb, id = id)
    
    except Exception as e: 
        return(str(e))

# @app.route('/', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, host="localhost")