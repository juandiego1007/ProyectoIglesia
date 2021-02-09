<?php 

class conexion{
 /**
  * Conexion a la base de datos
  */
	public static function conectar(){
		try {

			$cn =  new PDO("mysql:host=localhost;dbname=db","root","ecw12345");

			return $cn;

		} catch (PDOException $e) {
			die($ex->getmessage());
		}
	}

}

