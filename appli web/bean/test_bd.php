<?php
/**
 * Exemple simple qui étend la classe SQLite3 et change les paramètres
 * __construct, puis, utilise la méthode de connexion pour initialiser la
 * base de données.
 */
class MyDB extends SQLite3
{
    function __construct()
    {
        $this->open('my_base.db');
    }
}

$db = new MyDB();

$result = $db->query("SELECT ActivLibel FROM activites where ActivLibel='%oot%'");
var_dump($result->fetchArray());

?>