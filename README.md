# Proyecto_python

Proyecto de python: generador de contraseñas

Contexto:

Este proyecto lo hice con el objetivo de poder tener una mejor seguridad en nuestro acceso a cuentas de correo electrónico, al registrarnos en alguna aplicación o software, o en general para que la seguridad de las contraseñas que escribimos no sea fácil de ser vulneradas. 
Según un estudio de NordPass en el mundo la contraseña mas utilizada en el mundo es 123456, lo que significa que esta contraseña puede ser descifrada en menos de un segundo (NordPass, 2021).
Los errores que normalmente conocemos al escribir una contraseña son ponerle alguna fecha importante para nosotros como nuestra fecha de nacimiento, nuestro nombre u el de una persona conocida, números secuenciales u otro tipo de información personal. Para esto el proyecto genera contraseñas de forma aleatoria utilizando números, mayúsculas, minúsculas y caracteres especiales. 

Pseudocodigo:

Inicio (mayúsculas, minúsculas, números, caracteres especiales, contraseña, conjunto, lista, matriz, minusculas2) El conjunto contendrá minúsculas y números como estándar de la contraseña Pedir el tamaño de la contraseña
Se define la funcion de generar contraseñas
Se defina la funcion de guardar contraseña 
Se define la funcion de encriptar y desencriptar contraseñas
Se define la funcion de guardar mensaje encriptado
Mientras que opcion sea igual a 1 y menor que 7 se realizara:
  Se da opciones para elegir de un menu
  Si opcion = 1, se llama a la funcion de generar contrañas pidiendose el tamaño de la contraseña, si quiere que tenga mayusculas, si quiere que tenga carateres    especiales y el numero de contraseñas a generar.
  Si opcion = 2, se agrega la a una lista
  Si opcion = 3, se optienen las contrañas guardas en la lista
  Si opcion = 4, se encripta el texto dado por el usuario
  Si opcion = 5, se desencripta el texto
  Si opcion = 6, se imprimen los mensajes encriptados guardados anteriormente
  Si opcion = 7, se termina el programa
