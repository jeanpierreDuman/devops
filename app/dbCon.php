<?php

$user = "root";
$pass = "root";

try {
    $dbh = new PDO('mysql:host=host.docker.internal;dbname=devops_db;port=3306', $user, $pass);
//    $dbh = new PDO('mysql:host=127.0.0.1;dbname=devops_db;port=3306', $user, $pass);
} catch( Exception $e) {
    die($e->getMessage());
}