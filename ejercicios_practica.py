#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3
from typing import NamedTuple

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill(id, name, age, grade, tutor=""):
    # print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    values = [id,name, age, grade, tutor]

    c.execute("""
        INSERT INTO estudiante (id,name, age, grade, tutor)
        VALUES (?,?,?,?,?);""", values)

    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
    # Conectarse a la base de datos
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    # Leer todas las filas y obtener todos los datos juntos
    c.execute('SELECT * FROM estudiante')
    data = c.fetchall()
    print(data)
    
    for row in c.execute('SELECT * FROM estudiante'):
        print(row)
    
    conn.commit()

    conn.close()

def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    for row in c.execute("SELECT id, name, age FROM estudiante WHERE grade =?",(grade,)):
        print('Selección:', row)


    conn.commit()

    conn.close()


def insert(group):
    print('Nuevos ingresos!')

    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.executemany('''
                    INSERT INTO estudiante(id,name,age,grade,tutor)
                    VALUES(?,?,?,?,?);''',group )
    for row in c.execute('SELECT * FROM estudiante'):
        print(row)

    conn.commit()

    conn.close()


def modify(name, id):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    rowcount = c.execute("UPDATE estudiante SET name =? WHERE id =?",
                        (name, id)).rowcount

    print('Estudiante actualizado:', rowcount)

    conn.commit()
    
    conn.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    # fill()
    fill(1,'Pedro',18,6,'Inove')
    fill(2,'Juan',17,3,'Johana')
    fill(3,'Marina',18,6,'Hernán')
    fill(4,'Amancay',19,5,'Inove')
    fill(5,'Nelson',18,3,)
    fill(6,'Pedro',17,6,'Hernán')
    
    
    # fetch()
    fetch()

    grade = 3
    # search_by_grade(grade)
    search_by_grade(grade)

    # new_student = ['You', 16]
    # insert(new_student)
    group = [(7,'Maxy', 20, 5,'Inove'),
             (8,'Sandra', 18, 6, 'Hernán'),
             (9,'Pedro', 20, 4, 'Johana'),
             ]

    insert(group)

    id = 2
    name = '¿Inove?'

    # modify(id, name)
    modify(id, name)
