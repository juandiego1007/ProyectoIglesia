<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <title>Administracion pastor</title>
{% extends  "layout.html" %}

{% block content %}


<?php

  if(isset($_SESSION["usuario"])){
    if($_SESSION["usuario"]["privilegio"] == 1){
        header("location: congregacion.php");
    }
  }else{
    header("location:index.php");
  }
?>

<!-- First Container -->
<div class="container-fluid bg-1 text-center">
  <div class="row">
      <h1>Bienvenid@ <?php echo $_SESSION["usuario"]["nombre"]; ?></h1>
            <div class="container bg-white">
                <div class="row text-center h-100 bg-white d-flex justify-content-center align-items-center">
                  <h2>Cultos:</h2>
                  <br>
                  <div class="col-md-3">
                    <img src="img/modifica.png">
                    <h3>Listar</h3>
                  </div>
                  <div class="col-md-3">
                    <img src="img/lista.png">
                    <h3>Modificar</h3>
                  </div>
                  <div class="col-md-3">
                    <a href="phpflaskR.php">
                    <img src="img/calendario1.png">
                  </a>
                    <h3>Crear</h3>
                  </div>
                  <div class="col-md-3">
                    <img src="img/calendario20.png">
                    <h3>Eliminar</h3>
                  </div>
                </div>

                <div class="row text-center h-100 bg-white d-flex justify-content-center align-items-center">
                  <h2>Congregasión:</h2>
                  <br>
                  <div class="col-md-3">
                    <img src="img/modifica.png">
                    <h3>Listar</h3>
                  </div>
                  <div class="col-md-3">
                    <img src="img/lista.png">
                    <h3>Modificar</h3>
                  </div>
                  <div class="col-md-3">
                    <img src="img/calendario1.png">
                    <h3>Crear</h3>
                  </div>
                  <div class="col-md-3">
                    <img src="img/calendario20.png">
                    <h3>Eliminar</h3>
                  </div>
                </div>

            </div>
            <br>
        <a href="cerrar-sesion.php" class="btn btn-primary btn-lg">Cerrar Sesión</a>
  </div>
</div>


<!-- Footer -->
<footer class="container-fluid bg-4 text-center">
  <p>Copyright © 2020. All Rights Reserved</p>
</footer>

{% endblock %}
