import sqlite3

db_connection = sqlite3.connect('Alumnos1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'juan', 'garcia')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'ana', 'Rodriguez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'mario', 'erickson')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'carl', 'jonson')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'kiko', 'pele')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'monse', 'vasquez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'sofia', 'sidane')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'dan', 'chaves')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'juan'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()