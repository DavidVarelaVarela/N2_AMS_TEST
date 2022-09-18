BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Autores" (
	"AutorID"	INTEGER,
	"Nombre"	TEXT,
	"Apellidos"	TEXT,
	"FechaNacimiento"	TEXT,
	"Descripcion"	TEXT,
	PRIMARY KEY("AutorID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "LibrosEstado" (
	"EstadoID"	INTEGER,
	"NombreEstado"	TEXT UNIQUE,
	PRIMARY KEY("EstadoID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Libros" (
	"LibroID"	INTEGER,
	"Titulo"	TEXT,
	"AutorID"	INTEGER NOT NULL,
	"Editor"	TEXT,
	"FechaEdicion"	TEXT,
	"Costo"	NUMERIC,
	"EstadoID"	INTEGER,
	"Vendido"	INTEGER,
	PRIMARY KEY("LibroID" AUTOINCREMENT),
	FOREIGN KEY("EstadoID") REFERENCES "LibrosEstado"("EstadoID")
);
COMMIT;
