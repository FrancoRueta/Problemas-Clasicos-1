Sin alterar la clase listaFinita, modificar el programa de modo que el productor inserte objetos tupla de strings tomados al azar de la siguiente lista.


[("España","Madrid"), ("Francia","Paris"),("Italia","Roma"),("Inglaterra","Londres"),("Alemania","Berlin",("Rusia","Moscu"),
("Turquia","Istambul"),("China","Pekin"), ("Japon","Tokio"),("Emiratos Arabes","Dubai"),("Argentina","Buenos Aires"),
("Brasil","Brasilia"),("Colombia","Bogota"),("Uruguay","Montevideo")]

Esta lista contiene tuplas ("pais", "capital").

Modificar el consumidor de modo que imprima un mensaje: "La capital de "pais" es "capital".

Por ejemplo:

La capital de Argentina es Buenos Aires

El programa no debe mostrar inconsistencias ni errores debidos a condiciones de carrera o falta de sincronización.

Nota: para la impresión de mensajes utlizar preferentemente el módulo logging.