from flask import Flask, request, jsonify, render_template
from config import Config
import pyodbc

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obtener_datos_sql', methods=['GET'])
def obtener_datos_sql():
    cedula = request.args.get('cedula').replace("-", "")
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=201.237.248.149;DATABASE=PracticaUtilidades;UID=pruebas2016;PWD=pruebas2016'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('EXEC ObtenerDatosPorCedulaJoseGuzman ?', cedula)
    row = cursor.fetchone()
    if row:
        return jsonify(success=True, data={
            'nombre': row.nombre,
            'apellido1': row.apellido1,
            'apellido2': row.apellido2,
            'fechaNacimiento': row.fechaNacimiento
        })
    else:
        return jsonify(success=False, message='Cédula no encontrada.')

if __name__ == '__main__':
    app.run(debug=True)
