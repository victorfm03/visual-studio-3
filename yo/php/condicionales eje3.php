<?php

$hora=$_GET['Di una hora'];

$textoHora="[di un minuto]";

switch($hora){
    case "0":
    case "12":
        $textoHora ="doce";
        break;

    case "13":
    case "1":

        $textoHora ="una";
        break;
    case "14":
    case "2":

        $textoHora ="dos";
        break;
    
    case "15":
    case "3":

        $textoHora ="tres";
        break;
    
    case "16":
    case "4":

        $textoHora ="cuatro";
        break;

    case "17":
    case "5":

        $textoHora ="cinco";
        break;
    
    case "18":
    case "6":

        $textoHora ="seis";
        break;

    case "19":
    case "7":

        $textoHora ="siete";
        break;

    case "20":
    case "8":

        $textoHora ="ocho";
        break;

    case "21":
    case "9":

        $textoHora ="nueve";
        break;

    case "22":
    case "10":

        $textoHora ="diez";
        break;

    case "23":
    case "11":

        $textoHora ="once";
        break;
    
    default:
    print("hora no valida");

}

?>