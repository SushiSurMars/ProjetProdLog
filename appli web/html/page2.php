<?php

/* require once upon a time*/
require_once("../bean/dao.php");
require_once("../bean/Boite.php");

$activite = $_GET["activité"];
$commune = $_GET["commune"];

$dao = new dao();
$listeboite = $dao->liste($activite, $commune);

?>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="style/accueil.css" media="screen" />
</head>
<body>
	<div id="opacity">
	<img src="style/logo.png"  alt="logo">

	<h1>
	Bienvenue aux Pays de la Loire</h1>

	<?php foreach ($list as $boite) {
		# code...
	echo "<div id='boite' href=page3.php?activite=".$boite->getNomActivite()."&commune=".$boite->getNomCommune()."&numero=".$boite->getNumeroFiche()."> activité :".$boite->getNomActivite();
	echo "</br> commune :".$boite->getNomCommune();
	echo "</br> nom de l'installation:".$boite->getNomInstaltion();
	echo "</div>";
	} ?>


</div>
</body>
</html>