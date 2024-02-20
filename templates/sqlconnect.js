
export function addComment(comment) {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password"
    });

    con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");

    const dateTime = getDateTime();

    var sql = "INSERT INTO comments (ISBN, Comment, DateTime, User) VALUES ('" + isbn + "', '" + comment +"', '" + dateTime + "', testuser')";
    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("1 record inserted");
    });
});

}

export function redirect() {
    // alert();
    const searchTerm = document.getElementById('searchTerm').value.toLowerCase();
    const searchColumn = document.getElementById('searchColumn').value;
    // alert("search.html?q="+searchColumn+'&'+searchTerm);
    window.location.href="search.html?q="+searchColumn+'.'+searchTerm;
}

export function saveComment() {
    const userComment = document.getElementById('userComment').value;
    // alert(userComment);
    addComment(userComment);
    location.reload();

}