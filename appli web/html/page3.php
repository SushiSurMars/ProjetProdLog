<?php 
$activite = $_GET["activite"];
$commune = $_GET["commune"];
$numero = $_GET["numero"];

$dao = new dao();
$liste = $dao->information($activite,$commune,$numero);

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

	<div id="installation"> <?php
		echo "<p>nom de l'équipement :".$liste["nom_equipement"]."</p>";
	
		echo "<p>nom de l'installation :".$liste["nom_installation"]."</p>";
		
		echo "<p>activités :".$activite."</p>";
	
		echo "<p>niveau pratiqué :".$liste["niveau"]."</p>";
	
		echo "<p>adresse :".$liste["numero"]." ".$liste["rue"]."</p>";
		
		echo "<p>commune :".$commune."</p>";

		?>
	</div>

</div>
</body>
</html>