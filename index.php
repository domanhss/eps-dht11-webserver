<?php
$data = file_get_contents("data.json");
$json = json_decode($data, true);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dữ liệu cảm biến</title>
    <meta charset="utf-8">
</head>
<body>
    <h2>Dữ liệu từ ESP8266</h2>
    <p>Nhiệt độ: <strong><?php echo $json["temp"]; ?>°C</strong></p>
    <p>Độ ẩm: <strong><?php echo $json["humi"]; ?>%</strong></p>
    <p>Thời gian: <?php echo $json["time"]; ?></p>
</body>
</html>
