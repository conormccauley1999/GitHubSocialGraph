<?php

header("Content-Type: application/json");

$DB_SERVER 	= getenv('GH_DB_SERVER');
$DB_USER 	= getenv('GH_DB_USER');
$DB_PASS 	= getenv('GH_DB_PASS');
$DB_NAME 	= getenv('GH_DB_NAME');

if (isset($_POST["query"])) {
	$DB_QUERY = $_POST["query"];
} else {
	$DB_QUERY = "select 0 Error";
}

$conn = new mysqli($DB_SERVER, $DB_USER, $DB_PASS, $DB_NAME);
$result = array();

if ($rows = $conn->query($DB_QUERY)) {
	$temp = array();
	while ($row = $rows->fetch_object()) {
		$temp = $row;
		array_push($result, $temp);
	}
}

echo json_encode($result);

$rows->close();
$conn->close();

?>
