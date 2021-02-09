<!DOCTYPE html>
<html lang="en">
<head>
   <?php session_start();?>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <title>Reserva de Asistencia - Pastor</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
  <link rel="stylesheet" type="text/css" href="assets/css/overhang.min.css" />
  <script type="text/javascript" src="assets/js/overhang.min.js"></script>

  <script src="assets/js/app1.js"></script>

  <style>
  body {
    font: 20px Montserrat, sans-serif;
    line-height: 1.8;
    color: #f5f6f7;
  }
  p {font-size: 16px;}
  .margin {margin-bottom: 45px;}
  .bg-1 { 
    background-color: #81D4FA  ; 
    color: #ffffff;
  }
  .bg-4 { 
    background-color: #F8F9F9; /* Black Gray */
    color: #000000  ;
  }
  .container-fluid {
    padding-top: 70px;
    padding-bottom: 70px;
  }
  .navbar {
    padding-top: 15px;
    padding-bottom: 15px;
    border: 0;
    border-radius: 0;
    margin-bottom: 0;
    font-size: 12px;
    letter-spacing: 5px;
  }
  .navbar-nav  li a:hover {
    color: #1abc9c !important;
  }
  h3 {
    color: #000000;
  }
  h2 {
    text-align: left;
    color: #000000;
  }
  </style>
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-default">
  <div class="container bg-white">
      <div class="row text-center h-100 bg-white d-flex justify-content-center align-items-center">
        <div class="col-lg-4">
          <img src="img/logo1.png" width="300" height="auto">          
        </div>
        <div class="col-lg-4">
          <img src="img/logo4.png" width="350" height="auto">          
        </div>
        <div class="col-lg-4">
          <img src="img/logo3.png" width="80" height="auto">          
        </div>
      </div>
  </div>
</nav>

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
                    <img src="img/calendario1.png">
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

</body>
</html>