<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <title>Registro de usuario</title>


{% extends  "layout.html" %}

{% block content %}

<!-- First Container -->
<div class="container-fluid bg-1 text-left">
  <div class="row">
    <div class="col-md-4 col-md-offset-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <form id="registraU" action="registroCode.php" method="POST" role="form">
            <legend class="text-center">Registrarse</legend>

            <div class="form-group">
              <label for="nombre" class="text-left">Nombre</label>
              <input type="text" name="txtNombre" class="form-control" id="nombre"  required placeholder="Ingresa tú Nombre">
            </div>

            <div class="form-group">
              <label for="apellidos" class="text-left">Apellidos</label>
              <input type="text" name="txtApellido" class="form-control" id="apellido"  required placeholder="Ingresa tus Apellidos">
            </div>

            <div class="form-group">
              <label for="documento" class="text-left">Tipo de documento</label>
              <select name="txtTipoDocumento" id="tipoDocumento" class="form-control">
                    <option selected>Seleccione</option>
                    <option> Cédula de Ciudadanía</option>
                    <option> Tarjeta de Identidad</option>
                    <option> Cédula de Extranjería</option>
                    <option> Pasaporte</option>
              </select>
            </div>

            <div class="form-group">
              <label for="cedula" class="text-left">Número de Documento</label>
              <input type="text" name="txtDocumento" class="form-control" id="cedula"  required placeholder="Ingresa tú número de documento">
            </div>

            <div class="form-group">
              <label for="foto">Seleccione una foto</label>
              <input type="file" class="form-control-file" id="imagen" name="txtFoto">
            </div>

            <div class="form-group">
              <label for="fechaNacimiento" class="text-left">Fecha de Nacimiento</label>
              <input type="date" name="txtFechaNacimiento" class="form-control" id="fechaNacimiento"  required>
            </div>


            <div class="form-group">
              <label for="sexo" class="text-left">Sexo</label>
              <select name="txtGenero" id="genero" class="form-control">
                    <option selected>Seleccione</option>
                    <option> Mujer</option>
                    <option> Hombre</option>
              </select>
            </div>


            <div class="form-group">
              <label for="rh" class="text-left">RH</label>
              <select name="txtRh" id="rh" class="form-control">
                    <option selected>Seleccione</option>
                    <option> A+</option>
                    <option> A-</option>
                    <option> B+</option>
                    <option> B-</option>
                    <option> O+</option>
                    <option> O-</option>
                    <option> AB+</option>
                    <option> AB-</option>
              </select>
            </div>

            <div class="form-group">
              <label for="correo" class="text-left">Correo Electrónico</label>
              <input type="email" name="txtEmail" class="form-control" id="correo"  required placeholder="Ingresa tú Correo Electrónico">
            </div>

            <div class="form-group">
              <label for="celular" class="text-left">Número de celular</label>
              <input type="tel" name="txtCelular" class="form-control" id="celular"  required placeholder="Ingresa tú Número de celular">
            </div>

            <div class="form-group">
              <label for="direccion" class="text-left">Dirección</label>
              <input type="text" name="txtDireccion" class="form-control" id="direccion"  required placeholder="Ingresa tú Dirección">
            </div>

            <div class="form-group">
              <label for="tipoEstadoCivil" class="text-left">Estado Civil</label>
              <select name="txtEstadoCivil" id="tipoEstadoCivil" class="form-control">
                    <option selected>Seleccione</option>
                    <option> Soltero/a </option>
                    <option> Casado/a </option>
                    <option> Unión libre o unión de hecho </option>
                    <option> Separado/a </option>
                    <option> Divorciado/a </option>
                    <option> Viudo/a </option>
              </select>
            </div>

            <div class="form-group">
              <label for="eps" class="text-left">EPS/SISBEN</label>
              <input type="text" name="txtEps" class="form-control" id="epsSisben"  required placeholder="Ingresa tú EPS o Sisben">
            </div>

            <div class="form-group">
              <label for="tipoAsistente" class="text-left">Tipo Asistente</label>
              <select name="tipoAsistente" id="tipoAsistente" class="form-control">
                    <option value="">Seleccione</option>
                    <option value="as"> Amigo Simpatizante</option>
                    <option value="hb"> Hermano Bautizado</option>
              </select>
            </div>

            <div id="pai">

              <div id="hb" class="form-group">
                <label for="fechaBautizmo" class="text-left">Fecha de Bautizo</label>
                <input type="date" name="txtFechaBautizo" class="form-control" id="fechaBautizo">
              </div>

              <div id="hb" class="form-group">
                <label for="nombre" class="text-left">Nombre Pastor que lo Bautizó</label>
                <input type="text" name="txtNombrePastor" class="form-control" id="
                pastorBautizo"  placeholder="Ingresa el Nombre del Pastor">
              </div>

            </div>

            <div class="form-group">
              <label for="llenoSantoEs" class="text-left">¿Lleno del Espíritu Santo?</label>
              <select name="llenoSanto" id="llenoSanto" class="form-control">
                    <option value="">Seleccione</option>
                    <option value="si">Si</option>
                    <option value="no">No</option>
              </select>
            </div>

            <div id="pai2">
              <div id="s" class="form-group">
                <label for="fecha" class="text-left">Fecha de este</label>
                <input type="date" name="txtFechaSanto" class="form-control" id="fechaSanto">
              </div>
            </div>

            <div class="form-group">
              <label for="servidorEs" class="text-left">¿Es servidor local?</label>
              <select name="servidorLocal" id="servidorLocal" class="form-control">
                    <option value="">Seleccione</option>
                    <option value="si">Si</option>
                    <option value="no">No</option>
              </select>
            </div>

            <div id="pai3">
              <div id="si" class="form-group">
                <label for="comite" class="text-left">Comité</label>
                <input type="text" name="txtComite" class="form-control" id="comite"  placeholder="Ingresa tú Comité">
              </div>

              <div id="si" class="form-group">
                <label for="cargo" class="text-left">Cargo</label>
                <input type="text" name="txtCargo" class="form-control" id="cargo"  placeholder="Ingresa tú Cargo">
              </div>
            </div>

            <button type="submit" class="btn btn-primary btn-block">Registrarse</button>
            <a href="index.php" class="btn btn-success btn-block">Regresar</a>

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

{% endblock %}
