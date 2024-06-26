<?php

require_once "dbCon.php";

$sql = "insert into userNum(id) value (?)";
$stmt = $dbh->prepare($sql);
$stmt->execute([$_POST['num']]);

header("Location: index.php");