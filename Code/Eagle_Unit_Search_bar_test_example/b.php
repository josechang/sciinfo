<?php

$id = $_POST['id'];

echo "OK";
$fp_wpost = fopen("123.csv", "w");
$z  ="User input"."\n";
$z .=$id;
fputs($fp_wpost, $z);
fclose($fp_wpost); 
?>