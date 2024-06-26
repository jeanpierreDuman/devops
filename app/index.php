<?php

echo "Welcome to localhost serv from docker php";

require_once "dbCon.php";
echo "<p> --- </p>";

echo "<div id='listContent'>";
foreach($dbh->query("SELECT * FROM userNum") as $row) {
    echo $row['id'] . ' ';
}

echo "</div>";

require_once "form.html";