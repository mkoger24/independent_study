from flask import Flask, render_template, request, send_file, redirect, request#, abortr
import mysql.connector
import datetime
import string

# establish connection to sql server
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

@app.route('/home.html', methods=['GET',"POST"])
def home():
    # if the user performs a search from the home page, run the query and render the search page
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
        
        # if no specified search parameters, show all entries
        # this should, in theory, never execute as there will always be a column selected
            # so, do i need to keep this here?
        else:
            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"

        # run the query and return the template
        mycursor = mydb.cursor() 
        mycursor.execute(query) 
        dbhtml = mycursor.fetchall() 
        return render_template("search.html", dbhtml = dbhtml)
    
    # if method == 'GET' render home page
    return render_template("home.html")

@app.route('/login.html', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/search.html', methods=['GET','POST'])
def searchTerm():

    try: 
        # if there was a search, store column and searchTerm from form
        if request.method == "POST":
            column = request.form["searchColumn"]
            mysearch = request.form['searchTerm']
            print('column: ',column)
            print('searchTerm:', mysearch)
            
            searchTerm = ""
            for x in mysearch:
                if x == "'":
                    searchTerm = searchTerm + "'" + "'"
                else:
                    searchTerm += x

        
        # if there are no specified search parameters, display all entries
        else:
            if (request.args.get("q")):
                
                id = request.args.get("q")
                getAuthor = "SELECT Author FROM books WHERE id like " + id + ";"
                mycursor = mydb.cursor() 
                mycursor.execute(getAuthor) 
                authorTuple = mycursor.fetchall()
                authorList = authorTuple[0]
                authorString = authorList[0]

                query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books WHERE Author like '%" + authorString + "%';"
                mycursor = mydb.cursor() 
                mycursor.execute(query) 
                dbhtml = mycursor.fetchall() 
                return render_template("search.html", dbhtml = dbhtml)

            query = "SELECT id, ElectronicISBN, BookTitle, Author, CopyrightYear FROM books;"
            mycursor = mydb.cursor() 
            mycursor.execute(query) 
            dbhtml = mycursor.fetchall() 
            return render_template("search.html", dbhtml = dbhtml)

        # if no specified search parameters, show all entries
        # this should, in theory, never execute as there will always be a column selected
            # so, do i need to keep this here?
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
        
        # if no specified search parameters, show all entries
        # this should, in theory, never execute as there will always be a column selected
            # so, do i need to keep this here?
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
        # if the user enters a comment and/or tag
        if request.method == "POST":
            id = request.args.get("q")
            mycomment = request.form["userComment"]
            tag = request.form['userTag']

            # getting date and time for comment table
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

            comment = ""
            for x in mycomment:
                if x == "'":
                    comment = comment + "'" + "'"
                else:
                    comment += x
            print(comment)

            # if comment and tag are submitted
            if comment != '' and tag != '':

                query = "INSERT INTO comments (book_id, Comment, DateTime, User) VALUES ('" + id + "', '" + comment +"', '" + dateTime + "', 'testuser');"
                mycursor = mydb.cursor() 
                mycursor.execute(query)
                bookdb = mycursor.fetchall()
                mydb.commit() 

                query = "INSERT INTO tags () VALUES ('" + id + "', '" + tag +"');"
                mycursor = mydb.cursor() 
                mycursor.execute(query)
                bookdb = mycursor.fetchall()
                mydb.commit()  

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
            
            # if comment and no tag
            elif comment != '' and tag == '':

                query = "INSERT INTO comments (book_id, Comment, DateTime, User) VALUES ('" + id + "', '" + comment +"', '" + dateTime + "', 'testuser');"
                mycursor = mydb.cursor() 
                mycursor.execute(query) 
                bookdb = mycursor.fetchall() 
                mydb.commit() 

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
            
            # if tag and no comment
            elif comment == '' and tag != '': 

                query = "INSERT INTO tags () VALUES ('" + id + "', '" + tag +"');"
                mycursor = mydb.cursor() 
                mycursor.execute(query)
                bookdb = mycursor.fetchall() 
                mydb.commit() 

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

@app.route('/download')
def download():
    path = '2024_koger_mae.pdf'
    return send_file(path, as_attachment=True)

# @app.route('/', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, host="localhost")