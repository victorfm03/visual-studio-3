<!DOCTYPE html>
<html>

    <head>

    </head>

    <body>
        <form action="eje3.php">

        <input type="text" name="n1">
        <br>
        <input type="text" name="n2">
        <br>
        <input type="submit">

        </form>
        <?php

        if(isset($_GET['n1']) && isset($_GET['n2'])){
            $numeros=[];

            for ($a=0;$a<=100;$a++){
            
                $numeros[]=rand(0,20);
                
            }

            foreach ($numeros as $num){
                echo "<spam> $num </spam>";
            }

            $modify=[];
            foreach ($numeros as $num){

                if($num==$n1){
                    $modify[]=$n2;
                    echo "<spam> $num </spam>";
                }else{
                    $modify[]=$num;
                    echo "<spam> $num </spam>";
                }
                
            }

        }else{
            echo "indica un numero";
        }

        ?>
    </body>
</html>