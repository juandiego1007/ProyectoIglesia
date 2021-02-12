<?php

include '../../controlador/UsuarioControlador.php';
include '../../helps/helps.php';

//session_start();

//header('Content-type: application/json');
//$resultado = array();

if($_SERVER["REQUEST_METHOD"] == "POST"){
	if(isset($_POST["txtNombre"]) && isset($_POST["txtApellido"]) && isset($_POST["txtTipoDocumento"]) && isset($_POST["txtDocumento"]) && isset($_POST["txtFechaNacimiento"]) && isset($_POST["txtGenero"]) && isset($_POST["txtRh"]) && isset($_POST["txtEmail"]) && isset($_POST["txtCelular"]) && isset($_POST["txtDireccion"]) && isset($_POST["txtEstadoCivil"]) && isset($_POST["txtEps"]) && isset($_POST["tipoAsistente"]) && isset($_POST["txtFoto"])  && isset($_POST["txtFechaBautizo"]) && isset($_POST["txtNombrePastor"]) && isset($_POST["llenoSanto"]) && isset($_POST["txtFechaSanto"]) && isset($_POST["servidorLocal"]) && isset($_POST["txtComite"]) && isset($_POST["txtCargo"])){


	$txtNombre = validar_campo($_POST["txtNombre"]);
	$txtApellido = validar_campo($_POST["txtApellido"]);
	$txtTipoDocumento = validar_campo($_POST["txtTipoDocumento"]);
	$txtDocumento = validar_campo($_POST["txtDocumento"]);

	$txtFechaNacimiento = validar_campo($_POST["txtFechaNacimiento"]);
	$txtGenero = validar_campo($_POST["txtGenero"]);
	$txtRh = validar_campo($_POST["txtRh"]);
	$txtEmail = validar_campo($_POST["txtEmail"]);
	$txtCelular = validar_campo($_POST["txtCelular"]);
	$txtDireccion = validar_campo($_POST["txtDireccion"]);
	$txtEstadoCivil = validar_campo($_POST["txtEstadoCivil"]);
	$txtEps = validar_campo($_POST["txtEps"]);

	if (validar_campo($_POST["tipoAsistente"]) == "hb") {
		$txtTipoAsistente = "Hermano Bautizado";
	}else{
		$txtTipoAsistente = "Amigo Simpatizante";
	}

	$txtFechaBautizo = validar_campo($_POST["txtFechaBautizo"]);
	$txtNombrePastor = validar_campo($_POST["txtNombrePastor"]);

	if (validar_campo($_POST["llenoSanto"]) == "s") {
		$txtllenoSanto = "Si" ;
	}else{
		$txtllenoSanto = "No" ;
	}

	$txtFechaSanto = validar_campo($_POST["txtFechaSanto"]);
	$txtServidorLocal = validar_campo($_POST["servidorLocal"]);
	$txtComite = validar_campo($_POST["txtComite"]);
	$txtCargo = validar_campo($_POST["txtCargo"]);
	$txtPrivilegio = "1";
	$txtImagen = validar_campo($_POST["txtFoto"]);
	$txtPassword = $txtDocumento;


	    $nacimiento = new DateTime($txtFechaNacimiento);
	    $ahora = new DateTime(date("Y-m-d"));
	    $diferencia = $ahora->diff($nacimiento);

	$txtEdad = $diferencia->format("%y");

	$existe =  UsuarioControlador::validar($txtDocumento);


	if($existe == true){
			echo '<script language="javascript">alert("Usuario ya existe!!");</script>';
			header("Refresh:1; url=index.php");
	}else{

		if (UsuarioControlador::registrar($txtNombre, $txtApellido , $txtTipoDocumento, $txtDocumento, $txtPassword, $txtImagen, $txtEdad, $txtFechaNacimiento, $txtGenero, $txtRh, $txtTipoAsistente, $txtEmail, $txtCelular, $txtDireccion, $txtEstadoCivil, $txtEps, $txtFechaBautizo, $txtNombrePastor, $txtllenoSanto, $txtFechaSanto, $txtServidorLocal, $txtComite, $txtCargo, $txtPrivilegio)){

				echo '<script language="javascript">alert("Usuario Agregado Correctamente!!");</script>';
				header("Refresh:1; url=index.php");
		}
}


}else{
	header("location:registro.php?error=1");
	}
}
