<?php
$nombre= $_GET['txtNombre'];
$edad=$_GET['txtEdad'];

echo "Hola". htmlspecialchars($nombre) ."<br>";
echo "Tu edad es $edad";