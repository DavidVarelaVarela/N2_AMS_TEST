# Technical Test

* Se ha elegido sqlite como bbdd puesto que es compatible con cualquier Sistema Operativo y no hace falta un setup especial (Instalar un gestor bbdd) para poder trabajar con ella.

## Ejercicio 1: SQL
Se tiene una base de datos que contiene tres tablas: Autores, Libros y LibrosEstado como se muestra a continuación:

 ![Libreria Schema](/assets/libreria_schema.png)

Construya una consulta que recupere un conjunto de resultados con las columnas:
LibroID (Identificador del libro) y Titulo (Título del libro) de la tabla Libros y que recupere el nombre y apellido del autor asociado a cada libro. 

Dado que las columnas Nombre y Apellido del autor del libro se encuentra en la tabla Autores, se deben combinar las tablas Libros y la tabla Autores utilizando la columna AutorID en la condición de combinación.
Teniendo en cuenta que a columna AutorID es una clave foránea en la tabla Libros para la columna AutorID de la tabla Autores. El conjunto de resultados debe incluir sólo las primeras 20 filas con valores en la columna Costo de la tabla Libros mayores a 12.

```sql
SELECT l.LibroID, l.Titulo, a.Nombre, a.Apellidos
FROM Libros l JOIN Autores a
	ON l.AutorID = a.AutorID
WHERE l.Costo IS NOT NULL
LIMIT 20;
```
Nota: Costo puede ser NULL (no tiene por qué tener un precio cuando nos llega el libro al almacén por lo que se puede poner a posteriori)

## Ejercicio 3: SQL Server
Se tiene una base de datos que contiene tres tablas: Aplicacion, HistoricoEstadosAplicacion y EstadosAplicacion como se muestra a continuación:

![Libreria Schema](/assets/aplicacion_schema.png)

Construya una consulta que recupere un conjunto de resultados con las columnas: Nombre, Estado (Descripción del estado actual de la aplicación) y Fecha (Fecha del último cambio de estado).
```sql
SELECT a.Nombre, ea.Descripcion, h.FechaCambio
FROM Aplicacion a JOIN HistoricoEstadosAplicacion h
  ON a.IdAplicacion = h.IdAplicacion
JOIN EstadosAplicacion ea
  ON h.IdEstado = ea.IdEstado;