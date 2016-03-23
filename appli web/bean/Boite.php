<?php
/**
* objet permettant d avoir des informations de base sur une activitee et son installation
*/
class Boite
{
	
	function __construct($NomAct, $NomC, $NomInsta, $NumeroF)
	{
		$this ->NomActivite = $NomAct;
		$this ->NomCommune = $NomC;
		$this ->NomInstaltion = $NomInsta;
		$this ->NumeroFiche = $NumeroF;
	}

	function getNomActivite(){
		return $this->NomActivite;
	}

	function getNomCommune(){
		return $this->NomCommune;
	}

	function getNomInstaltion(){
		return $this->NomInstaltion;
	}

	function getNumeroFiche(){
		return $this->NumeroFiche;
	}
}
?>