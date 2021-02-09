<?php

include '../datos/UsuarioDao.php';

class UsuarioControlador{

	public static function login($cedula,$password){
		$obj_usuario = new Usuario();
		$obj_usuario->setCedula($cedula);
		$obj_usuario->setPassword($password);

		return UsuarioDao::login($obj_usuario);
	}

	public function getUsuario($cedula,$password){
		$obj_usuario = new Usuario();
		$obj_usuario->setCedula($cedula);
		$obj_usuario->setPassword($password);

		return UsuarioDao::getUsuario($obj_usuario);
	}


	public function validar($cedula){

		$obj_usuario = new Usuario();
		$obj_usuario->setCedula($cedula);

		return UsuarioDao::validar($obj_usuario);
	}

	public function registrar($nombre, $apellido, $tipoDocumento, $cedula, $password, $imagen, $edad, $fechaNacimiento, $genero, $rh, $tipoAsistente, $correo, $celular, $direccion, $estadoCivil, $epsSisben, $fechaBautizmo, $pastorBautizmo, $llenoSanto, $fecha, $servidorLocal, $comite, $cargo, $privilegio){

		$obj_usuario = new Usuario();
		$obj_usuario->setNombre($nombre);
		$obj_usuario->setApellido($apellido);
		$obj_usuario->setTipoDocumento($tipoDocumento);
		$obj_usuario->setCedula($cedula);
		$obj_usuario->setPassword($password);
		$obj_usuario->setImagen($imagen);
		$obj_usuario->setEdad($edad);
		$obj_usuario->setFechaNacimiento($fechaNacimiento);
		$obj_usuario->setGenero($genero);
		$obj_usuario->setRh($rh);
		$obj_usuario->setTipoAsistente($tipoAsistente);
		$obj_usuario->setCorreo($correo);
		$obj_usuario->setCelular($celular);
		$obj_usuario->setDireccion($direccion);
		$obj_usuario->setEstadoCivil($estadoCivil);
		$obj_usuario->setEpsSisben($epsSisben);
		$obj_usuario->setFechaBautizmo($fechaBautizmo);
		$obj_usuario->setPastorBautizo($pastorBautizmo);
		$obj_usuario->setLlenoSanto($llenoSanto);
		$obj_usuario->setFecha($fecha);
		$obj_usuario->setServidorLocal($servidorLocal);
		$obj_usuario->setComite($comite);
		$obj_usuario->setCargo($cargo);
		$obj_usuario->setPrivilegio($privilegio);

		return UsuarioDao::registrar($obj_usuario);
	}

}