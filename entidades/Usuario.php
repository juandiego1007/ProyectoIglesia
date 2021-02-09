<?php

Class Usuario{

	private $id;
	private $nombre;
	private $apellido;
	private $tipoDocumento;
	private $cedula;
	private $password;
	private $imagen;
	private $edad;
	private $fechaNacimiento;
	private $genero;
	private $rh;
	private $tipoAsistente;
	private $correo;
	private $direccion;
	private $celular;
	private $estadoCivil;
	private $epsSisben;
	private $bautizado;
	private $fechaBautizmo;
	private $pastorBautizo;
	private $llenoSanto;
	private $fecha;
	private $servidorLocal;
	private $comite;
	private $cargo;
	private $privilegio;


	public function getId(){
		return $this->id;
	}

	public function setId($id){
		$this->id = $id;
	}

	public function getNombre(){
		return $this->nombre;
	}

	public function setNombre($nombre){
		$this->nombre = $nombre;
	}

	public function getApellido(){
		return $this->apellido;
	}

	public function setApellido($apellido){
		$this->apellido = $apellido;
	}

	public function getTipoDocumento(){
		return $this->tipoDocumento;
	}

	public function setTipoDocumento($tipoDocumento){
		$this->tipoDocumento = $tipoDocumento;
	}

	public function getCedula(){
		return $this->cedula;
	}

	public function setCedula($cedula){
		$this->cedula = $cedula;
	}

	public function getPassword(){
		return $this->password;
	}

	public function setPassword($password){
		$this->password = $password;
	}

	public function getImagen(){
		return $this->imagen;
	}

	public function setImagen($imagen){
		$this->imagen = $imagen;
	}

	public function getEdad(){
		return $this->edad;
	}

	public function setEdad($edad){
		$this->edad = $edad;
	}

	public function getFechaNacimiento(){
		return $this->fechaNacimiento;
	}

	public function setFechaNacimiento($fechaNacimiento){
		$this->fechaNacimiento = $fechaNacimiento;
	}

	public function getGenero(){
		return $this->genero;
	}

	public function setGenero($genero){
		$this->genero = $genero;
	}

	public function getRh(){
		return $this->rh;
	}

	public function setRh($rh){
		$this->rh = $rh;
	}

	public function getTipoAsistente(){
		return $this->tipoAsistente;
	}

	public function setTipoAsistente($tipoAsistente){
		$this->tipoAsistente = $tipoAsistente;
	}

	public function getCorreo(){
		return $this->correo;
	}

	public function setCorreo($correo){
		$this->correo = $correo;
	}

	public function getCelular(){
		return $this->celular;
	}

	public function setCelular($celular){
		$this->celular = $celular;
	}

	public function getDireccion(){
		return $this->direccion;
	}

	public function setDireccion($direccion){
		$this->direccion = $direccion;
	}

	public function getEstadoCivil(){
		return $this->estadoCivil;
	}

	public function setEstadoCivil($estadoCivil){
		$this->estadoCivil = $estadoCivil;
	}

	public function getEpsSisben(){
		return $this->epsSisben;
	}

	public function setEpsSisben($epsSisben){
		$this->epsSisben = $epsSisben;
	}

	public function getFechaBautizmo(){
		return $this->fechaBautizmo;
	}

	public function setFechaBautizmo($fechaBautizmo){
		$this->fechaBautizmo = $fechaBautizmo;
	}

	public function getPastorBautizo(){
		return $this->pastorBautizo;
	}

	public function setPastorBautizo($pastorBautizo){
		$this->pastorBautizo = $pastorBautizo;
	}

	public function getLlenoSanto(){
		return $this->llenoSanto;
	}

	public function setLlenoSanto($llenoSanto){
		$this->llenoSanto = $llenoSanto;
	}

	public function getFecha(){
		return $this->fecha;
	}

	public function setFecha($fecha){
		$this->fecha = $fecha;
	}

	public function getServidorLocal(){
		return $this->servidorLocal;
	}

	public function setServidorLocal($servidorLocal){
		$this->servidorLocal = $servidorLocal;
	}

	public function getComite(){
		return $this->comite;
	}

	public function setComite($comite){
		$this->comite = $comite;
	}

	public function getCargo(){
		return $this->cargo;
	}

	public function setCargo($cargo){
		$this->cargo = $cargo;
	}

	public function getPrivilegio(){
		return $this->privilegio;
	}

	public function setPrivilegio($privilegio){
		$this->privilegio = $privilegio;
	}

}