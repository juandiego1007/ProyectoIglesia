<?php

include 'conexion.php';
include '../entidades/Usuario.php';

class UsuarioDao extends conexion{

	protected static $cnx;

	private static function getconexion(){
		self::$cnx = conexion::conectar();
	}

	private static function desconectar(){
		self::$cnx = null;
	}

/**
 * metodo para validar login
 */
	public static function login($usuario){

		$query = "SELECT * FROM usuarios where cedula = :cedula AND password = :password";

		self::getconexion();

		$resultado = self::$cnx->prepare($query);

		$resultado->bindValue(":cedula",$usuario->getCedula());
		$resultado->bindValue(":password",$usuario->getPassword());

		$resultado->execute();

		if($resultado->rowCount() > 0){
			$filas = $resultado->fetch();
			if ($filas["cedula"] == $usuario->getCedula() && $filas["password"] == $usuario->getPassword() ) {
				return true;
			}
		}

		return false;
	}


/**
 * metodo para obtener usuario
 */
	public static function getUsuario($usuario){

		$query = "SELECT nombre,apellido,privilegio FROM usuarios where cedula = :cedula AND password = :password";

		self::getconexion();

		$resultado = self::$cnx->prepare($query);

		$resultado->bindValue(":cedula",$usuario->getCedula());
		$resultado->bindValue(":password",$usuario->getPassword());

		$resultado->execute();

		$filas = $resultado->fetch();

		$usuario = new Usuario();
		$usuario->setNombre($filas["nombre"]);
		$usuario->setApellido($filas["apellido"]);
		$usuario->setPrivilegio($filas["privilegio"]);
		
		return $usuario;
	}


	public static function validar($usuario){

		$query = "SELECT * FROM usuarios where cedula = :cedula";

		self::getconexion();

		$resultado = self::$cnx->prepare($query);

		$resultado->bindValue(":cedula",$usuario->getCedula());


		$resultado->execute();

		if($resultado->rowCount() > 0){
			$filas = $resultado->fetch();
			if ($filas["cedula"] == $usuario->getCedula()) {
				return true;
			}
		}

		return false;
	}


/**
 * metodo para Registrar
 */
	public static function registrar($usuario){

		$query = "INSERT INTO usuarios (nombre, apellido, tipoDocumento, cedula, password, imagen, edad, fechaNacimiento, genero, rh, tipoAsistente, correo, celular, direccion, estadoCivil, epsSisben, fechaBautizmo, pastorBautizo, llenoSanto, fecha, servidorLocal, comite, cargo, privilegio) VALUES (:nombre, :apellido, :tipoDocumento, :cedula, :password, :imagen, :edad, :fechaNacimiento, :genero, :rh, :tipoAsistente, :correo, :celular, :direccion, :estadoCivil, :epsSisben, :fechaBautizmo, :pastorBautizo, :llenoSanto, :fecha, :servidorLocal, :comite, :cargo, :privilegio)";

		self::getconexion();

		$resultado = self::$cnx->prepare($query);

		$resultado->bindValue(":nombre",$usuario->getNombre());
		$resultado->bindValue(":apellido",$usuario->getApellido());
		$resultado->bindValue(":tipoDocumento",$usuario->getTipoDocumento());
		$resultado->bindValue(":cedula",$usuario->getCedula());
		$resultado->bindValue(":password",$usuario->getPassword());
		$resultado->bindValue(":imagen",$usuario->getImagen());
		$resultado->bindValue(":edad",$usuario->getEdad());
		$resultado->bindValue(":fechaNacimiento",$usuario->getFechaNacimiento());
		$resultado->bindValue(":genero",$usuario->getGenero());
		$resultado->bindValue(":rh",$usuario->getRh());
		$resultado->bindValue(":tipoAsistente",$usuario->getTipoAsistente());
		$resultado->bindValue(":correo",$usuario->getCorreo());
		$resultado->bindValue(":celular",$usuario->getCelular());
		$resultado->bindValue(":direccion",$usuario->getDireccion());
		$resultado->bindValue(":estadoCivil",$usuario->getEstadoCivil());
		$resultado->bindValue(":epsSisben",$usuario->getEpsSisben());
		$resultado->bindValue(":fechaBautizmo",$usuario->getFechaBautizmo());
		$resultado->bindValue(":pastorBautizo",$usuario->getPastorBautizo());
		$resultado->bindValue(":llenoSanto",$usuario->getLlenoSanto());
		$resultado->bindValue(":fecha",$usuario->getFecha());
		$resultado->bindValue(":servidorLocal",$usuario->getServidorLocal());
		$resultado->bindValue(":comite",$usuario->getComite());
		$resultado->bindValue(":cargo",$usuario->getCargo());
		$resultado->bindValue(":privilegio",$usuario->getPrivilegio());

		if ($resultado->execute()) {
			return true;
		}

		return false;
	}

}