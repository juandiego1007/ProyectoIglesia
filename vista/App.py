from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_assets  import Environment, Bundle
import  bcrypt
import datetime
from datetime import date,datetime

app = Flask(__name__)




# Proceso terminar de cambiar todo php a py
# Quede en registrar usuario y no he probado nada


assetss = Environment(app)

css = Bundle('css/bootstrap.min.css','css/main.css')
assetss.register('css_all', css)

js = Bundle('js/popper,min.js', 'js/bootstrap.min.js')
assetss.register('js_all', js)

asset = Bundle('assets/css/overhang.min.css', 'assets/js/overhang.min.js' , 'assets/js/app1.js', 'assets/js/app2.js')
assetss.register('assets_all', asset)

img = Bundle('img/logo1.png', 'img/logo4.png', 'img/logo3.png')
assetss.register('img_all', img)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ecw12345'
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)
app.secret_key = "EsunSecret0"

semilla = bcrypt.gensalt()

@app.route('/')
def Rindex():
    if 'nombre' in session:
        return render_template('')
    else:
        return render_template('index.html')


@app.route('/pastor')
def Rpastor():
    if 'nombre' in session:
        return render_template('')
    else:
        return render_template('')

@app.route('/registro')
def Rregistrousuario():
    return render_template('registro.html')

@app.route('/registroCode', methods=['POST'])
def Mregistrousuario():

# Hace falta recuperar, guardar y devolver las imagenes https://www.tutorialspoint.com/file-upload-example-in-python
# https://codigosimportantes.blogspot.com/2012/09/almacenar-y-recuperar-fotos-desde-mysql.html

    if request.method == 'POST':
        nombre = "'" + request.form['txtNombre'] + "'"
        apellido = "'" + request.form['txtApellido'] + "'"
        tipodocumento = "'" + request.form['txtTipoDocumento'] + "'"
        numerodocumento = "'" + request.form['txtDocumento'] + "'"
        passtempencode = request.form['txtDocumento'].encode("utf-8")
        passtempencripted = bcrypt.hashpw(passtempencode, semilla)
        password = "'" + str(passtempencripted.decode('utf-8')) + "'"

        foto =  "'" + request.form['txtFoto'] + "'"
        print(foto)

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
        cur.execute("INSERT INTO usuarios (nombre, apellido, tipoDocumento, cedula, password, imagen, edad ,fechaNacimiento, genero, rh, tipoAsistente, correo, celular, direccion, estadoCivil, epsSisben, fechaBautizmo, pastorBautizo, llenoSanto, fecha, servidorLocal, comite, cargo, privilegio) VALUES (" +
        nombre + " , "  + apellido + ","  + tipodocumento + " , "  + numerodocumento + " , " + password + ", "+ foto + " , "+ edad + " , "  +
        fechanacimiento + " , "  + sexo + " , "  + rh + " , "  + tipoasistente + " , "  + email + " , "  + celular + " , "  + direccion + " , "  +
        estadocivil + " , "  + eps + " , "  + fechabautizo + " , "  + nombrepastor + " , "  + llenosanto + " , "  + fechasanto + " , "  +
        servidorlocal + " , "  + comite + " , "  + cargo + " , "  + privilegio + ")")
        mysql.connection.commit()
        return render_template('index.html')

    else:
        return render_template('index.html')



@app.route('/Crearculto')
def CrearcultoTemplate():
    return render_template('Crearculto.html')
@app.route('/CrearcultoAction', methods=['POST'])
def CrearcultoAction():
    if request.method == 'POST':
        fecha = "'" + request.form['txtFecha'] + "'"
        horainicio ="'" + request.form['txthorainicio'] + "'"
        horafinal ="'" + request.form['txthorafinal'] + "'"
        capacidadmax = request.form['txtcapacidadmax']
        piso = request.form['txtpiso']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO culto (fecha, horainicio, horafinal, capacidadmax, piso) VALUES (' +  fecha  + ' , ' + horainicio + ',' + horafinal  + ' ,' + capacidadmax + ',' + piso + ')')
        mysql.connection.commit()
        return render_template()

    else:
        pass

if __name__ == '__main__':
    app.run(debug=True) #En modo de prueba, para que se reinicie solo
