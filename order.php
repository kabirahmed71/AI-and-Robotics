<?php
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    header("Location: index.php");
    exit;
}

$name = trim($_POST["name"] ?? "");
$phone = trim($_POST["phone"] ?? "");
$item = trim($_POST["item"] ?? "");
$qty = trim($_POST["qty"] ?? "");
$address = trim($_POST["address"] ?? "");
$payment = trim($_POST["payment"] ?? "");

if ($name === "" || $phone === "" || $item === "" || $qty === "" || $address === "" || $payment === "") {
    header("Location: index.php");
    exit;
}

$message = "Order from PUST Central Cafe:\n";
$message .= "Name: " . $name . "\n";
$message .= "Phone: " . $phone . "\n";
$message .= "Item: " . $item . "\n";
$message .= "Qty: " . $qty . "\n";
$message .= "Address: " . $address . "\n";
$message .= "Payment: " . $payment;

$whatsAppNumber = "88039384";
$url = "https://wa.me/" . $whatsAppNumber . "?text=" . rawurlencode($message);

header("Location: " . $url);
exit;
?>
