from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

class Conexion:
    def __init__(self):
        self.host = 'ls-794fe89f337bd7e30918d1ad53ab0afd5f091f11.cwjr2a47qc0n.us-east-1.rds.amazonaws.com'
        self.port = 3306
        self.user = 'dbmasteruser'
        self.password = '<^BR*3CR22rB;tdo8S?$pts#f>9mZms1'
        self.database = 'BD1'

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print('Conecta')
                self.cursor = self.connection.cursor()
        except Error as e:
            print('Error en la conexión con la base de datos', e)
    
    def consultar_estudiantes(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            consulta = "SELECT * FROM Estudiante;"
            self.cursor.execute(consulta)
            estudiantes = self.cursor.fetchall()
            return estudiantes
    
    def consultar_catedraticos(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            consulta = "SELECT * FROM Catedratico;"
            self.cursor.execute(consulta)
            catedraticos = self.cursor.fetchall()
            return catedraticos

@app.route('/')
def consulta():
    con = Conexion()
    con.conectar()
    estudiantes = con.consultar_estudiantes()
    catedraticos = con.consultar_catedraticos()
    return render_template('principal.html', estudiantes=estudiantes, catedraticos=catedraticos)

if __name__ == '__main__':
    app.run()