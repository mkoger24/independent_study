<?php
  $servername = "localhost";
  $username = "root";
  $password = "password";
  $dbname = "snbooks";

  $conn = new mysqli($servername, $username, $password, $dbname);
  if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
  } 

  $sql = "SELECT ElectronicISBN, BookTitle, Author, SeriesTitle, ProductType, FROM books";
  $result = $conn->query($sql);

  <tr align="center">
      <th>Electronic ISBN</th>
      <th>Book Title</th>
      <th>Author</th>
      <th>Series Title</th>
      <th>Product Type</th>
  </tr>
  echo "<table><tr><th>table headding</th></tr>";
  while($row = $result->fetch_assoc()) {

      echo    "<tr><td><strong>ISBN:</strong></td><td>" .$row["ElectronicISBN"]. "</td></tr>";
      echo    "<tr><td><strong>BookTitle:</strong></td><td>" .$row["BookTitle"]."</td></tr>";
      echo    "<tr><td><strong>Author:</strong></td><td>" .$row["Author"]. "</td></tr>";
      echo    "<tr><td><strong>Series Title:</strong></td><td>" .$row["SeriesTitle"]."</td></tr>" ;
      echo    "<tr><td><strong>Product Type:</strong></td><td>" .$row["ProductType"]."</td></tr>" ;
      echo    "<tr><td><br><br></td></tr>";

  }
  echo "</table>";
?>