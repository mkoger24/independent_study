
let SpringerNatureBooks = fetch("SpringerNatureBooks.json")
.then(function(response){
    return response.json();
})
.then((SpringerNatureBooks)=>{
    // let placeholder = document.querySelector("#data-output");
    // let out = "";
    // for(let SpringerNatureBook of SpringerNatureBooks)
    let data1=`<tr>
        <th>ISBN</th>
        <th>Title</th>
        <th>Author</th>
        <th>Edition</th>
        </tr>`;
    SpringerNatureBooks.map((values)=>{
        data1+=`
            <tr>
                <td>${values.PrintISBN}</td>
                <td>${values.BookTitle}</td>
                <td>${values.Author}</td>
            </tr>
        `;
    });
    document.getElementById("table").innerHTML=data1;
});