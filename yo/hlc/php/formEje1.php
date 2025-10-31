<?php

$numero=$_GET['txtNumero'];


for ($a=1;$a<=10;$a++){

    echo($numero. "*".$a."=". $a*$numero."<br>");

}