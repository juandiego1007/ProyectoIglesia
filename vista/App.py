from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_assets  import Environment, Bundle
import  bcrypt
import datetime
from datetime import date,datetime, timedelta

app = Flask(__name__)

# set de assets para toas las paginas html de la aplicacion
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
# final de assets


# configuracion e inicializacion de mysql and flask
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ecw12345'
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

# set para clave secreta. se usa para enviar mensajes por flash y para las cookies
app.secret_key = "EstaEsun1Contr4@"


# semilla usada para encriptar y desencriptar las contraseñas
semilla = bcrypt.gensalt()

# Usado para establecer el tiempo limite para que una sesion se caduque
app.permanent_session_lifetime = timedelta(minutes=5)


# Metodo madre, retorna la pagina principal del sitio

@app.route('/')
def Rindex():

    if 'nombre' in session and session['privis'] == 1 :
        return redirect(url_for('Rusuario'))
    elif 'nombre' in session and session['privis'] == 2:
        return redirect(url_for('Rpastor'))

    else:
        return render_template('index.html')



# registro de usuario general

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


# iniciar sesion de usuario general

@app.route('/iniciosesion', methods=['POST'])
def Miniciosesion():
    if 'nombre' in session:
        return redirect(url_for('Rindex'))

    else:

        if request.method == 'POST':
            cedula =  "'" + request.form['txtCedula'] + "'"
            password =  request.form['txtPassword']

            cur = mysql.connection.cursor()
            cur.execute('select cedula, password, privilegio, nombre, apellido from usuarios where cedula='+cedula+' LIMIT 1;')
            resultado = cur.fetchone()
            mysql.connection.commit()

            print(resultado)

            if resultado != None:

                passencodedDB = resultado[1].encode('utf-8')
                passencodeHTML = password.encode('utf-8')

                Parseprivilegio = int(resultado[2])

                print(passencodedDB)
                print(resultado[2])

                try:
                    if (bcrypt.checkpw(passencodeHTML,passencodedDB)):
                        if Parseprivilegio == 2:
                            session.permanent = True  # <--- makes the permanent session
                            session['nombre'] = resultado[3] + resultado[4]
                            session['privis'] = 2
                            session['cedula'] = int(resultado[0])

                            return redirect(url_for('Rpastor'))
                        elif Parseprivilegio == 1 :
                            session.permanent = True  # <--- makes the permanent session
                            session['nombre'] = resultado[3] + resultado[4]
                            session['privis'] = 1
                            session['cedula'] = int(resultado[0])

                            return redirect(url_for('Rusuario'))
                        print(session)

                        # registrar la session
                        # return redirect(url_for(''))


                    else:
                        flash('La contraseña o la cedula estan incorrectas', 'alert-danger')
                        return redirect(url_for('Rindex'))

                except ValueError:
                    flash('Error en la encriptacion','alert-danger')
                    return redirect(url_for('Rindex'))

            else:
                flash('No existe el usuario', 'alert-danger')
                return redirect(url_for('Rindex'))

        else:

            return redirect(url_for('Rindex'))

# cerrar sesion de usuario general

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




        # Metodos para el pastor###############################################################################################################

@app.route('/pastor')
def Rpastor():
    if 'nombre' in session and session['privis'] == 2:

        return render_template('/pastor.html')
    else:
        return redirect(url_for('Rindex'))

# retornamos la pagina solocitada, en este caso para buscar cultos donde
# se proporciona un input tipo fecha

@app.route('/busquedadecultos')
def Rbusquedadecultos():
    if 'nombre' in session and session['privis'] == 2:

        return render_template('busquedadecultos.html')
    else:
        flash('No tiene permisos suficientes', 'alert-danger')
        return redirect(url_for('Rindex'))


# recivimos la fecha enviada desde el metodo anterior y comenzamos el proceso de formato estandar
# luego de tener la fecha en formato, comenzamos a averiguar si hay algun culto desde la fecha enviada hasta 7 dias
# despues, evaluando cada minuto que tiene el dia. finalmente guardamos lo que la sentencia sql nos de y la enviamos
# como parametro para ser usado en otra pagina
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


# retornamos el formulario para registrar un culto nuevo

@app.route('/Crearculto')
def CrearcultoTemplate():
    if 'nombre' in session and session['privis'] == 2:
        return render_template('Crearculto.html')
    else:
        flash('No tiene permisos suficientes', 'alert-danger')
        return redirect(url_for('Rindex'))


# recibimos los datos enviados para registrar el culto, ejecutamos la sentencia sql para registro y retornamos a la pagina principal
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


# retornamos la pagina encargada de solicitar una fecha para hacer la busqueda

@app.route('/buscarcultoM')
def RbuscarcultoM():
    if 'nombre' in session and session['privis'] == 2:

        return render_template('buscarcultoM.html')
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

# obtenemos la fecha del metodo anterior y le hacemos un proceso de formato,
# luego al igual que en los anteriores metodos, evaluamos 7 dias apartir de la fecha que el usuarios
# ingreso y tambien cada minuto del dia. finalmente guardamos los resultados que arroja la base de datos
# y devolvemos los resultados como parametro para ser usado depues

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

# obtenemos el id del culto que se desea modificar(el seleccionado) y comenzamos la busqueda de la informacion. finalmente enviamos los datos
# del culto que se selecciono y se envian como paramentro para ser usado en proceso por parte del navegador del usuario

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


# ahora recibimos los cambios que el pastor deseo hacer sobre el culto y ejecutamos la sentencia de sql para
# actualizar registros

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


# obtenemos el id del culto que el pastor selecciono para ser eliminado
# y ejecutamos la sentencia sql para eliminar el registro en la base de datos

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



@app.route('/buscarusuario')
def Mbuscarusuario():
    if 'nombre' in session and session['privis'] == 2:
        return render_template('buscarusuario.html')

    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/mostrarusuario', methods=['POST'])
def Mmostrarusuario():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':
            cedulaobtenida = request.form['txtcedula']
            cur = mysql.connection.cursor()
            existe = cur.execute('select nombre,apellido,tipoDocumento, cedula, edad, genero, tipoAsistente, correo, celular' +
            ', direccion, estadoCivil, fechaBautizmo, pastorBautizo, llenoSanto, fecha, servidorLocal, comite, cargo, privilegio, idUsuario ' +
            ' from usuarios where cedula=' + str(cedulaobtenida) )
            if existe != 0:
                resultado = cur.fetchone()
                print(resultado)
                mysql.connection.commit()
                return render_template('Rmostrandousuario.html', resultado=resultado)
            else:
                flash('No existe el usuario solicitado!', 'alert-danger')
                return redirect(url_for('Rindex'))


        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/ModificarUser', methods=['POST'])
def RmostraruserP():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':
            id = request.form['txtidd']
            print(id)
            cur = mysql.connection.cursor()
            print('select cargo, celular, comite, correo, direccion, epsSisben' +
            ', estadoCivil, fechaBautizmo, llenoSanto, pastorBautizo, servidorLocal, tipoAsistente ' +
            ' from usuarios where idUsuario=' + str(id))
            existe = cur.execute('select cargo, celular, comite, correo, direccion, epsSisben' +
            ', estadoCivil, fechaBautizmo, llenoSanto, pastorBautizo, servidorLocal, tipoAsistente ' +
            ' from usuarios where idUsuario=' + str(id))
            if existe !=0:
                resultado = cur.fetchone()
                mysql.connection.commit()

                return render_template('Rmodificandousuario.html', resultado=resultado, id=id)

            else:
                flash('Usuario solicitado no existe!', 'alert-danger')
                return redirect(url_for('Rpastor'))

        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/MterminarmodificacionUser', methods=['POST'])
def MterminarmodificacionUser():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':
            lista = []
            for i in range(12):
                lista.append("'"+ str(request.form['txt'+str(i)]) + "'")


            id = request.form['txtid']
            cur = mysql.connection.cursor()
            print(lista)

            cur.execute('UPDATE  usuarios SET cargo={0}, celular={1}, comite={2}, correo={3}, direccion={4}, epsSisben={5}, estadoCivil={6}, fechaBautizmo={7}, llenoSanto={8}, pastorBautizo={9}, servidorLocal={10}, tipoAsistente={11}'.format(*lista)
               + ' WHERE idUsuario='+ str(id) )



            mysql.connection.commit()
            flash('Usuario modificado con exito!', 'alert-success')
            return redirect(url_for('Rpastor'))

        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))






@app.route('/Rmostrandousuario')
def Rmostrandousuario():
    if 'nombre' in session and session['privis'] == 2:
        return redirect(url_for('Rmostrandousuario.html'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))



@app.route('/buscarusuariocita')
def Rbuscarusuariocita():
    if 'nombre' in session and session['privis'] == 2:
        return render_template("buscarusuariocita.html")
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/Mbuscarusuariocita', methods=['POST'])
def Mbuscarusuariocita():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':
            cedulaobtenida = "'" + request.form['txtcedula'] + "'"
            if cedulaobtenida != None:
                cur = mysql.connection.cursor()
                existe = cur.execute('select idUsuario,nombre, apellido, cedula from usuarios where cedula=' + cedulaobtenida)
                if existe != 0:
                    resultado = cur.fetchone()
                    mysql.connection.commit()

                    flash('Usuario encontrado con exito!', 'alert-success')
                    return render_template('Rcrearconsulta.html',resultado=resultado)
                else:
                    flash('Usuario no encontrado!', 'alert-danger')
                    return redirect(url_for('Rindex'))
            else:
                flash('Llene el campo de la cedula!', 'alert-danger')
                return redirect(url_for('Mbuscarusuariocita'))
        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))


@app.route('/Mcrearconsulta', methods=['POST'])
def Mcrearconsulta():
    if 'nombre' in session and session['privis'] == 2:
        if request.method == 'POST':

            categoriaobtenida = "'" + request.form['txtcategoria'] + "'"
            importanciaobtenida = "'" + request.form['txtimportancia'] + "'"
            descripcionobtenida = "'" + request.form['txtdescripcion'] + "'"
            idobtenido = request.form['txtidusuario']

            today = str(date.today())
            date_time_obj = ("'"+str(datetime.strptime(today, '%Y-%m-%d'))+"'")


            cur = mysql.connection.cursor()
            try:
                cur.execute('INSERT INTO Consulta (idUsuario, categoria, descripcion, importancia, fecha) VALUES ('+ str(idobtenido)  +' ,' +str(categoriaobtenida)+' ,'+str(descripcionobtenida) +' ,'+ str(importanciaobtenida)+' ,'+ str(date_time_obj) +')')
                mysql.connection.commit()
                flash('Consulta registrada exitosamente!', 'alert-succesr')
                return redirect(url_for('Rindex'))

            except ValueError:
                flash('Error. No se pudo registrar la consulta','alert-danger')
                return redirect(url_for('Rindex'))
        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/Rlistarconsultas')
def Rlistarconsultas():
    if 'nombre' in session and session['privis'] == 2:
        return render_template("Rlistarconsultas.html")
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))
@app.route('/Mlistarconsultas', methods=['POST'])
def Mlistarconsultas():
    if 'nombre' in session and 'privis' == 2:
        if request.method == 'POST':
            fechainicio = request.form['txtfechainicio']
            cedulaobtenida = request.form['txtcedula']

            cur = mysql.connection.cursor()

            format = '%H:%M'


            date_time_obj = datetime.strptime(fechainicio, '%Y-%m-%d')

            # fechaconformato =  datetime.date(fechainicio[0:4],fechainicio[5:7],fechainicio[8:10])
            unlist = ()
            cantidad = 0
            statico = 0

            for i in range(7):


                fechaensuma = date_time_obj + timedelta(days=i)


                encontro = cur.execute("select C.idConsulta,C.idUsuario, C.categoria, C.descripcion, C.importancia, C.fecha from Consulta as C INNER JOIN usuarios as U ON C.idUsuario = U.idUsuario WHERE c.fecha=" + "'" + str(fechaensuma.date()) + "' " + " AND U.cedula ="+ str(cedulaobtenida) + "ORDER BY fecha")


                if(encontro != 0 ):
                    unlist +=  cur.fetchone()
                    cantidad +=1


            return render_template('Rlistadeconsultas.html', cantidad=cantidad, unlist=unlist)
        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))

    else:

        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))


@app.route('/modificarconsultaM', methods={'POST'})
def modificarconsultaM():
    if 'nombre' in session and 'privis' == 2:
        if request.method == 'POST':
            idobtenido = request.form['txtid']

            cur = mysql.connection.cursor()
            existe = cur.execute('select * from Consulta where idConsulta='+str(idobtenido))
            if existe != 0:

                resultado = cur.fetchone()
                render_template('Rmodificarconsulta.html',resultado=resultado)
            else:
                flash('No se encontro consulta!', 'alert-danger')
                return redirect(url_for('Rpastor'))
        else:
            flash('Accion no permitida!', 'alert-danger')
            return redirect(url_for('Rpastor'))

    else:

        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))

@app.route('/Rmodificarconsulta')
def Rmodificarconsulta():
    if 'nombre' in session and session['privis'] == 2:
        return render_template("Rmodificarconsulta.html")
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))








        # METODOS PARA EL USUARIO ###############################################################################################################


@app.route('/usuario')
def Rusuario():
    if 'nombre' in session and session['privis'] == 1:
        return render_template('Usuario.html')
    else:
        return redirect(url_for('Rindex'))

# Retornamos la pagina solicitada
@app.route('/buscarcultosU')
def RBuscarcultosU():
    if 'nombre' in session and session['privis'] == 1:
        return render_template('buscarcultosU.html')
    else:
        flash('No tiene permisos suficientes!', 'alert-danger')
        return redirect(url_for('Rindex'))


# Obtenemos la fecha enviada para buscar una reserva, la formatamos  y finalmente comenzamos
# a verificar si existe alguna reserva desde la fecha ingresada hasta 7 dias despues
# contando cada minuto de un dia
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


# Obtenemos la informacion del hidden input y comenzamos verificando la capacidad maxima
# de esta manera sabemos si el usuario puede reserbar asistencia
# en caso de que si, obtenemos los datos del usuario y con ella hacemos la consulta sql
# para registrar la reserva

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


# Retornamos la pagina html solicitada

@app.route('/listarasistenciasU')
def listarasistenciasU():
    if 'nombre' in session and session['privis'] == 1:
        return render_template('listarasistenciasU.html')
    else:
        flash('No tiene permisos!', 'alert-danger')
        return redirect(url_for('Rusuario'))

# hacemos el mismop proceso del metodo anterior para listar las reservas
# en este caso queremos saber

@app.route('/MlistarasistenciasU', methods=['POST'])
def MlistarasistenciasU():
    if 'nombre' in session and session['privis'] == 1:
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

                        query = ("SELECT culto.idCulto, culto.fecha, culto.horainicio, culto.horafinal, culto.capacidad, culto.capacidadmax, culto.piso FROM culto " +
                        "INNER JOIN reserva ON culto.idCulto = reserva.idCulto INNER JOIN usuarios on usuarios.idUsuario = reserva.IdUsuario  WHERE  culto.fecha=" + "'" + str(fechaensuma.date()) +
                        "' " + " AND culto.horainicio="+ "'"+ str(tiempoabuscar.time()) +"'" + "ORDER BY fecha, horainicio")
                        encontro = cur.execute(query)


                        if(encontro != 0 ):
                            unlist +=  cur.fetchone()
                            cantidad +=1


            return render_template('infoasistenciasU.html', cantidad=cantidad, unlist=unlist)
        else:
            flash('Solicitud no aceptada!', 'alert-danger')
            return redirect(url_for('Rusuario'))
    else:
        flash('No tiene permisos!', 'alert-danger')
        return redirect(url_for('Rusuario'))

# comenzamos verificando los datos del usuario en la sesion y con esos datos eliminamos el registro en la tabla de reservas
# luego al ser eliminado de reservas se debe actualizar en la tabla de cultos la capacidad que tiene el culto.
# por tanto solicitamos el valor de capacidad del culto y le restamos una asistencia.
# finalmente ejecutamos el update con la nueva capacidad que queda en el culto

@app.route('/eliminarasistenciaU', methods=['POST'])
def eliminarasistenciaU():
    if 'nombre' in session and session['privis'] == 1:
        if request.method == 'POST':

            cur = mysql.connection.cursor()
            query = ("select idUsuario from usuarios where cedula="+ str(session['cedula']))
            resultado = cur.execute(query)

            if resultado !=0:
                idusuario = cur.fetchone()
                idculto = request.form['txtid']
                query1 = ("DELETE from reserva  WHERE idCulto=" + str(idculto)  + " and idUsuario =" + str(idusuario[0]))
                cur.execute(query1)
                query2 = ("select capacidad from culto where idCulto=" + str(idculto))
                cur.execute(query2)
                capacidad = cur.fetchone()

                query3 = ("update culto set capacidad=" + str(capacidad[0]-1) + " where idCulto=" + str(idculto))
                cur.execute(query3)

                mysql.connection.commit()

                flash('Eliminacion realizada con exito!', 'alert-success')
                return redirect(url_for('Rusuario'))
            else:
                flash('No existe el usuario!', 'alert-danger')
                return redirect(url_for('Rusuario'))
        else:
            flash('Solicitud no aceptada!', 'alert-danger')
            return redirect(url_for('Rusuario'))
    else:
        flash('No tiene permisos!', 'alert-danger')
        return redirect(url_for('Rusuario'))







if __name__ == '__main__':
    app.run(debug=True) #En modo de prueba, para que se reinicie solo
