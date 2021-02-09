<?php

include '../controlador/UsuarioControlador.php';
include '../helps/helps.php';
$resultado = array();

session_start();

header('Content-type: application/json');

if($_SERVER["REQUEST_METHOD"] == "POST"){
	if(isset($_POST["txtCedula"]) && isset($_POST["txtPassword"])){

	$txtCedula = validar_campo($_POST["txtCedula"]);
	$txtPassword = validar_campo($_POST["txtPassword"]);

	$resultado = array("estado"=>"true");

	if (UsuarioControlador::login($txtCedula, $txtPassword)){
		
		$usuario = UsuarioControlador::getUsuario($txtCedula, $txtPassword);
		$_SESSION["usuario"] = array(
			"nombre" =>$usuario->getNombre(),
			"apellido" => $usuario->getApellido(),
			"privilegio" => $usuario->getPrivilegio(),
		);
		return print(json_encode($resultado));
	}

   }
}

$resultado = array("estado"=>"false");
return print(json_encode($resultado));