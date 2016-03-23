<?php
	require_once("ConnexionException.php");
	require_once("AccesTableException.php");
	//require_once __DIR__."";

	class Dao {
		private $connexion;

		public function connexion() {
	   		try {
			//connection
			$this->connexion = new PDO('mysql:host=localhost;charset=UTF8;dbname=E145437J','E145437J','E145437J');	//on se connecte au sgbd
			$this->connexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);	//on active la gestion des erreurs et d'exceptions
		    }
		    catch(PDOException $e) {
			throw new ConnexionException("Erreur de connection");
		    }
	    }

	 	public function deconnexion() {
	  		$this->connexion = null;
	  	}
	
	}
?>