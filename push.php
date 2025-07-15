<?php
date_default_timezone_set('Asia/Ho_Chi_Minh');

$temp = $_POST['temp'];
$humi = $_POST['humi'];
$time = date("Y-m-d H:i:s");

$data = array(
    "temp" => $temp,
    "humi" => $humi,
    "time" => $time
);

file_put_contents("data.json", json_encode($data));
echo "OK";
?>
