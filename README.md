# Proyecto_python

Proyecto de python: generador de contraseñas

Contexto:

Este proyecto lo hice con el objetivo de poder tener una mejor seguridad en nuestro acceso a cuentas de correo electrónico, al registrarnos en alguna aplicación o software, o en general para que la seguridad de las contraseñas que escribimos no sea fácil de ser vulneradas. 
Según un estudio de NordPass en el mundo la contraseña mas utilizada en el mundo es 123456, lo que significa que esta contraseña puede ser descifrada en menos de un segundo (NordPass, 2021).
Los errores que normalmente conocemos al escribir una contraseña son ponerle alguna fecha importante para nosotros como nuestra fecha de nacimiento, nuestro nombre u el de una persona conocida, números secuenciales u otro tipo de información personal. Para esto el proyecto genera contraseñas de forma aleatoria utilizando números, mayúsculas, minúsculas y caracteres especiales. 

Pseudocodigo:

EO (mayúsculas, minúsculas, números, caracteres especiales, contraseña, conjunto)
	El conjunto contendrá minúsculas y números como estándar de la contraseña 
	Pedir el tamaño de la contraseña  
	Pedir el si quiere que tenga caracteres especiales la contraseña 
	Pedir el si quiere que tenga mayúsculas
	Si quiere caracteres especiales, sumarle al conjunto caracteres especiales 
		Si no entonces no modificar el conjunto
 	Si quiere mayúsculas, sumarle al conjunto mayúsculas
Si no entonces no modificar el conjunto
	Generar una contraseña de manera random y teniendo en cuenta su tamaño solicitado
	Guardar la contraseña generada en la variable contraseña
EF (Imprimir la contraseña)
