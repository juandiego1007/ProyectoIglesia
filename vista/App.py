from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_assets  import Environment, Bundle

app = Flask(__name__)

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



@app.route('/')
def Rindex():
    return render_template('index.php')
@app.route('/validarCode.php')
def Rvalidarcode():
    return redirect(url_for('validarCode.php'))





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
