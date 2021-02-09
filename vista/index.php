<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <title>Reserva de Asistencia</title>
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

<!-- First Container -->
<div class="container-fluid bg-1 text-center">
  <div class="row">
    <div class="col-md-4 col-md-offset-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <form id="loginForm" action="validarCode.php" method="POST" role="form">
            <legend>Iniciar Sesión</legend>
            <div class="form-group">
              <input type="text" name="txtCedula" class="form-control" id="cedula" requiered placeholder="Cedula">
              <input type="password" name="txtPassword" class="form-control" id="password" requiered placeholder="Contraseña">
            </div>
            <button type="submit" class="btn btn-primary btn-block">Ingresar</button>
            <a href="registro.php" class="btn btn-success btn-block">Registrarse</a>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>


<!-- Footer -->
<footer class="container-fluid bg-4 text-center">
  <p>Copyright © 2020. All Rights Reserved</p>
</footer>

</body>
</html>
