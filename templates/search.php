<?php

$search = $_POST['search'];
$column = $_POST['column'];

$servername = "localhost";
$username = "root";
$password = "password";
$db = "bookLib";

$conn = new mysqli($servername, $username, $password, $db);

if ($conn->connect_error){
	die("Connection failed: ". $conn->connect_error);
}

$sql = "select * from bookLib.books where $column like '%$search%'";

$result = $conn->query($sql);

if ($result->num_rows > 0){
while($row = $result->fetch_assoc() ){
	echo $row["ElectronicISBN"]."  ".$row["BookTitle"]."  ".$row["Author"]."<br>";
}
} else {
	echo "0 records";
}

$conn->close();

?>