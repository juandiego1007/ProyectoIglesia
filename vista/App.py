from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_assets  import Environment, Bundle
import  bcrypt
import datetime
from datetime import date,datetime, timedelta

app = Flask(__name__)




# Proceso terminar de cambiar todo php a py
# Quede en registrar usuario y no he probado nada


assetss = Environment(app)

css = Bundle('css/bootstrap.min.css','css/main.css')
assetss.register('css_all', css)

js = Bundle('js/popper,min.js', 'js/bootstrap.min.js')
assetss.register('js_all', js)

assetcss = Bundle('../assets/css/overhang.min.css')
assetss.register('assets_1', assetcss)

assetjs = Bundle( '../assets/js/overhang.min.js' , '../assets/js/app1.js', '../assets/js/app2.js')
assetss.register('assets_2',assetjs)

img = Bundle('img/logo1.png', 'img/logo4.png', 'img/logo3.png')
assetss.register('img_all', img)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ecw12345'
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)
app.secret_key = "EstaEsun1Contr4@"

semilla = bcrypt.gensalt()

app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def Rindex():

    if 'nombre' in session and session['privis'] == 1 :
        return redirect(url_for('Rusuario'))
    elif 'nombre' in session:
        return redirect(url_for('Rpastor'))

    else:
        return render_template('index.html')


@app.route('/pastor')
def Rpastor():
    if 'nombre' in session and session['privis'] == 2:

        return render_template('/pastor.html')
    else:
        return redirect(url_for('Rindex'))


@app.route('/registro')
def Rregistrousuario():
    if 'nombre' in session:
        return redirect(url_for('Rindex'))
    else:
        return render_template('registro.html')


@app.route('/registroCode', methods=['POST'])
def Mregistrousuario():

# Hace falta recuperar, guardar y devolver las imagenes https://www.tutorialspoint.com/file-upload-example-in-python
# https://codigosimportantes.blogspot.com/2012/09/almacenar-y-recuperar-fotos-desde-mysql.html

    if 'nombre' in session:
        return redirect(url_for('Rindex'))

    else:
        if request.method == 'POST':
            nombre = "'" + request.form['txtNombre'] + "'"
            apellido = "'" + request.form['txtApellido'] + "'"
            tipodocumento = "'" + request.form['txtTipoDocumento'] + "'"
            numerodocumento = "'" + request.form['txtDocumento'] + "'"
            passtempencode = request.form['txtDocumento'].encode("utf-8")
            passtempencripted = bcrypt.hashpw(passtempencode, semilla)
            password = "'" + str(passtempencripted.decode('utf-8')) + "'"

            foto =  "'" + request.form['txtFoto'] + "'"


            fechanacimiento = "'" + request.form['txtFechaNacimiento'] + "'"
            fechatemp = ((request.form['txtFechaNacimiento']))
            date_time_obj = datetime.strptime(fechatemp, '%Y-%m-%d')
            edadentero =  int(((datetime.now().date() - date_time_obj.date()).days/365))
            edad = "'" + str(edadentero) + "'"



            sexo = "'" + request.form['txtGenero'] + "'"
            rh = "'" + request.form['txtRh'] + "'"
            email = "'" + request.form['txtEmail'] + "'"
            celular = "'" + request.form['txtCelular'] + "'"
            direccion = "'" + request.form['txtDireccion'] + "'"
            estadocivil = "'" + request.form['txtEstadoCivil'] + "'"
            eps = "'" + request.form['txtEps'] + "'"
            tipoasistente = "'" + request.form['tipoAsistente'] + "'"
            fechabautizo = "'" + request.form['txtFechaBautizo'] + "'"
            nombrepastor = "'" + request.form['txtNombrePastor'] + "'"
            llenosanto = "'" + request.form['llenoSanto'] + "'"
            fechasanto = "'" + request.form['txtFechaSanto'] + "'"
            servidorlocal = "'" + request.form['servidorLocal'] + "'"
            comite = "'" + request.form['txtComite'] + "'"
            cargo = "'" + request.form['txtCargo'] + "'"

            privilegio =  "'" + '1' + "'"
            cur = mysql.connection.cursor()
            # Verificamos si ya existe un usuario con esos datos


            if cur.execute("select * from usuarios where cedula="+numerodocumento) == 0:
                cur.execute("INSERT INTO usuarios (nombre, apellido, tipoDocumento, cedula, password, imagen, edad ,fechaNacimiento, genero, rh, tipoAsistente, correo, celular, direccion, estadoCivil, epsSisben, fechaBautizmo, pastorBautizo, llenoSanto, fecha, servidorLocal, comite, cargo, privilegio) VALUES (" +
                nombre + " , "  + apellido + ","  + tipodocumento + " , "  + numerodocumento + " , " + password + ", "+ foto + " , "+ edad + " , "  +
                fechanacimiento + " , "  + sexo + " , "  + rh + " , "  + tipoasistente + " , "  + email + " , "  + celular + " , "  + direccion + " , "  +
                estadocivil + " , "  + eps + " , "  + fechabautizo + " , "  + nombrepastor + " , "  + llenosanto + " , "  + fechasanto + " , "  +
                servidorlocal + " , "  + comite + " , "  + cargo + " , "  + privilegio + ")")
                mysql.connection.commit()
                flash("El usuario se registro existosamente. Inicie sesion", "alert-success")
                return redirect(url_for('Rindex'))
            else:
                flash("El usuario ya se encuentra registrado. Inicie sesion", "alert-danger")
                return redirect(url_for('Rindex'))


            cur.close()
        # en caso de no ser post lo devolvemos
        else:
            return render_template('index.html')


@app.route('/usuario')
def Rusuario():
    if 'nombre' in session and session['privis'] == 1:
        return render_template('Usuario.html')
    else:
        return redirect(url_for('Rindex'))

@app.route('/iniciosesion', methods=['POST'])
def Miniciosesion():
    if 'nombre' in session:
        return redirect(url_for('Rindex'))

    else:

        if request.method == 'POST':
            cedula =  "'" + request.form['txtCedula'] + "'"
            password =  request.form['txtPassword']

            cur = mysql.connection.cursor()
            cur.execute('select cedula, password, privilegio, nombre, apellido from usuarios where cedula='+cedula)
            resultado = cur.fetchone()
            mysql.connection.commit()

            if resultado != None:

                passencodedDB = resultado[1].encode('utf-8')
                passencodeHTML = password.encode('utf-8')


                print(passencodedDB)


                if (bcrypt.checkpw(passencodeHTML,passencodedDB)):
                    if(resultado[2]==2):
                        session.permanent = True  # <--- makes the permanent session
                        session['nombre'] = resultado[3] + resultado[4]
                        session['privis'] = 2
                        session['cedula'] = int(resultado[0])

                        return redirect(url_for('Rpastor'))
                    else:
                        session.permanent = True  # <--- makes the permanent session
                        session['nombre'] = resultado[3] + resultado[4]
                        session['privis'] = 1
                        session['cedula'] = int(resultado[0])
                        print(session)
                        return redirect(url_for('Rusuario'))

                    # registrar la session
                    # return redirect(url_for(''))


                else:
                    flash('La contraseña o la cedula estan incorrectas', 'alert-danger')
                    return redirect(url_for('Rindex'))

            else:
                flash('No existe el usuario', 'alert-danger')
                return redirect(url_for('Rindex'))

        else:

            return redirect(url_for('Rindex'))

@app.route('/cerrarsesion')
def Mcerrarsesion():
    if 'nombre' in session:
        session.pop('nombre', None)
        session.pop('privis', None)
        session.pop('cedula', None)
        flash('Sesion cerrada con exito!', 'alert-success')
        print(session)
        return redirect(url_for('Rindex'))

    else:
        flash('No tiene permisos suficientes', 'alert-danger')
        return redirect(url_for('Rindex'))


@app.route('/busquedadecultos')
def Rbusquedadecultos():
    if 'nombre' in session and session['privis'] == 2:

        return render_template('busquedadecultos.html')
    else:
        flash('No tiene permisos suficientes', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/listarcultos', methods=['POST'])
def Mlistarcultos():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':

            fechainicio = request.form['txtfechainicio']


            cur = mysql.connection.cursor()
            horaminimo = '00:00'
            format = '%H:%M'
            horaminimoform = datetime.strptime(horaminimo, format)

            date_time_obj = datetime.strptime(fechainicio, '%Y-%m-%d')

            # fechaconformato =  datetime.date(fechainicio[0:4],fechainicio[5:7],fechainicio[8:10])
            unlist = ()
            cantidad = 0
            statico = 0

            for i in range(7):
                for n in range(24):
                    for h in range(60):

                        tiempoabuscar = horaminimoform+timedelta(hours=n,minutes=h)

                        fechaensuma = date_time_obj + timedelta(days=i)


                        encontro = cur.execute("select fecha, horainicio, horafinal, capacidad, capacidadmax, piso from culto where fecha=" + "'" + str(fechaensuma.date()) + "' " + " AND horainicio="+ "'"+ str(tiempoabuscar.time()) +"'" + "ORDER BY fecha, horainicio")

                        if(encontro != 0 ):
                            unlist +=  cur.fetchone()
                            cantidad +=1


            return render_template('listarcultos.html', cantidad=cantidad, unlist=unlist)
        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rindex'))

    else:

        flash('No tiene permisos suficientes', 'alert-danger')
        return redirect(url_for('Rindex'))




@app.route('/Crearculto')
def CrearcultoTemplate():
    if 'nombre' in session and session['privis'] == 2:
        return render_template('Crearculto.html')
    else:
        flash('No tiene permisos suficientes', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/CrearcultoAction', methods=['POST'])
def CrearcultoAction():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':
            fecha = "'" + request.form['txtFecha'] + "'"
            horainicio ="'" + request.form['txthorainicio'] + "'"
            horafinal ="'" + request.form['txthorafinal'] + "'"
            capacidadmax = request.form['txtcapacidadmax']
            piso = request.form['txtpiso']

            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO culto (fecha, horainicio, horafinal, capacidadmax, piso) VALUES (' +  fecha  + ' , ' + horainicio + ',' + horafinal  + ' ,' + capacidadmax + ',' + piso + ')')
            mysql.connection.commit()

            flash('Culto creado con exito!', 'alert-success')
            return redirect(url_for('Rpastor'))


        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rindex'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))


@app.route('/buscarcultoM')
def RbuscarcultoM():
    if 'nombre' in session and session['privis'] == 2:

        return render_template('buscarcultoM.html')
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/modificarcultos' , methods=['POST'])
def Mmodificarcultos():
    if 'nombre' in session and 'privis' == 2:
        if request.method == 'POST':
            fechainicio = request.form['txtfechainicio']


            cur = mysql.connection.cursor()
            horaminimo = '00:00'
            format = '%H:%M'
            horaminimoform = datetime.strptime(horaminimo, format)

            date_time_obj = datetime.strptime(fechainicio, '%Y-%m-%d')

            # fechaconformato =  datetime.date(fechainicio[0:4],fechainicio[5:7],fechainicio[8:10])
            unlist = ()
            cantidad = 0
            statico = 0

            for i in range(7):
                for n in range(24):
                    for h in range(60):

                        tiempoabuscar = horaminimoform+timedelta(hours=n,minutes=h)

                        fechaensuma = date_time_obj + timedelta(days=i)


                        encontro = cur.execute("select idCulto, fecha, horainicio, horafinal, capacidad, capacidadmax, piso from culto where fecha=" + "'" + str(fechaensuma.date()) + "' " + " AND horainicio="+ "'"+ str(tiempoabuscar.time()) +"'" + "ORDER BY fecha, horainicio")

                        if(encontro != 0 ):
                            unlist +=  cur.fetchone()
                            cantidad +=1


            return render_template('modificarculto.html', cantidad=cantidad, unlist=unlist)
        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))

    else:

        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))


@app.route('/modificarcultoM', methods=['POST'])
def MmodificarcultoM():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':
            seleccionid = request.form['txtid']

            cur = mysql.connection.cursor()

            cur.execute("select fecha, horainicio, horafinal, capacidad, capacidadmax, piso from culto where idCulto=" + seleccionid)
            valores = cur.fetchone()

            return render_template('modificarcultoM.html', valores=valores, seleccionid=seleccionid)

        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))


@app.route('/Cambiarculto', methods=['POST'])
def Mcambiarculto():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':

            fecha = "'" + request.form['txtFecha'] + "'"
            horainicio ="'" + request.form['txthorainicio'] + "'"
            horafinal ="'" + request.form['txthorafinal'] + "'"
            capacidadmax = request.form['txtcapacidadmax']
            piso = request.form['txtpiso']
            id = request.form['txtid']

            cur = mysql.connection.cursor()
            cur.execute('UPDATE  culto SET fecha=' +  fecha  + ', horainicio=' + horainicio + ', horafinal=' + horafinal + ', capacidadmax=' + capacidadmax + ', piso=' + piso + ' WHERE idCulto='+ id )
            mysql.connection.commit()

            flash('Culto modificado con exito!', 'alert-success')
            return redirect(url_for('Rpastor'))

        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))

    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))


@app.route('/eliminarculto', methods=['POST'])
def Meliminarculto():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':
            id = request.form['txtid']
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM  culto  WHERE idCulto='+ id )
            mysql.connection.commit()

            flash('Culto eliminado con exito!', 'alert-success')
            return redirect(url_for('Rpastor'))

        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))

    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))



        # METODOS PARA EL USUARIO

@app.route('/buscarcultosU')
def RBuscarcultosU():
    if 'nombre' in session and session['privis'] == 1:
        return render_template('buscarcultosU.html')
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))



@app.route('/listarcultosUU', methods=['POST'])
def MlistarcultosUU():
    print('entro a listarcultos sin priv')
    if 'nombre' in session and session['privis'] == 1:
        print('entro a listarcultos con priv')
        if request.method == 'POST':
            fechainicio = request.form['txtfechainicio']


            cur = mysql.connection.cursor()
            horaminimo = '00:00'
            format = '%H:%M'
            horaminimoform = datetime.strptime(horaminimo, format)

            date_time_obj = datetime.strptime(fechainicio, '%Y-%m-%d')

            # fechaconformato =  datetime.date(fechainicio[0:4],fechainicio[5:7],fechainicio[8:10])
            unlist = ()
            cantidad = 0
            statico = 0

            for i in range(7):
                for n in range(24):
                    for h in range(60):

                        tiempoabuscar = horaminimoform+timedelta(hours=n,minutes=h)

                        fechaensuma = date_time_obj + timedelta(days=i)


                        encontro = cur.execute("select idCulto, fecha, horainicio, horafinal, capacidad, capacidadmax, piso from culto where fecha=" + "'" + str(fechaensuma.date()) + "' " + " AND horainicio="+ "'"+ str(tiempoabuscar.time()) +"'" + "ORDER BY fecha, horainicio")

                        if(encontro != 0 ):
                            unlist +=  cur.fetchone()
                            cantidad +=1


            return render_template('SeleccioncultoU.html', cantidad=cantidad, unlist=unlist)
        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rusuario'))

    else:

        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/SeleccioncultoU', methods=['POST'])
def MseleccionarcultoU():
    if 'nombre' in session and session['privis']==1:

        if request.method == 'POST':
            idculto = request.form['txtid']
            cur = mysql.connection.cursor()
            cur.execute('select capacidad, capacidadmax from culto where idCulto='+str(idculto))
            capacidad = cur.fetchone()
            print(capacidad)

            if capacidad[0]<=capacidad[1]:

                existe = cur.execute('select idUsuario from usuarios where cedula=' + "'" +str(session['cedula']) + "'")
                resultado = cur.fetchone()
                print(resultado)
                if existe != 0:
                    cur.execute('insert into reserva (idCulto, idUsuario) values (' + str(idculto) + ' , ' +  str(resultado[0]) + ')')
                    cur.execute('update culto set capacidad='+ str(capacidad[0]+1) + ' where idculto=' + str(idculto))
                    mysql.connection.commit()
                    flash('Asistencia registrada!', 'alert-success')
                    return redirect(url_for('Rusuario'))
                else:
                    flash('No existe el usuario!', 'alert-danger')
                    return redirect(url_for('Rusuario'))
            else:
                flash('Capacidad maxima excedida. No se pudo regitrar la asistencia!', 'alert-danger')
                return redirect(url_for('Rusuario'))
        else:
            flash('Solicitud no aceptada!', 'alert-danger')
            return redirect(url_for('Rusuario'))
    else:
        flash('No tiene permisos!', 'alert-danger')
        return redirect(url_for('Rusuario'))

if __name__ == '__main__':
    app.run(debug=True) #En modo de prueba, para que se reinicie solo
