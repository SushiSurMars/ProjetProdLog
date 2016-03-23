<?php

	class Dao extends SQLite3 {

	   function __construct(){
			$this->open('my_base.db');
	    }

	 	public function deconnexion() {
	  		$this->close();
	  	}

	  	public function liste($acti, $commu) {
	  		$stmt = $this->query("SELECT ActivCode FROM activites WHERE ActivLibel='".$acti."%"."' and NomCommune ='".$commu."';");
			print_r($stmt->fetchArray());
	  	}
	
	}

///TEST///
$dao = new Dao();

$dao->liste("Randonnée equestre","Anetz");

?>