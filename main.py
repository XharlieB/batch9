from alumno import Alumno

def start():
	add()

guardarAlumnos = []	

def add():
	preguntaQueHacer = input('Que deseas hacer? \n (1) Agregar un alumno. \n (2) Ver alumnos. \n (3) Salir \n  ')
	if preguntaQueHacer == '1':
		def camposNecesarios():
			nombreUsuario  = input('Ingresa el nombre(s) de tu Alumno: ')
			nombreAppend = nombreUsuario
			apellidoUsuario = input('Ingresa el Apellido(s) de tu Alumno: ')
			cintaUsuario = input('Ingresa la cinta de tu Alumno: ')
			edadUsuario = input('Ingresa la edad de tu Alumno: ')
			nombreAppend =  Alumno(nombreUsuario, apellidoUsuario, cintaUsuario, edadUsuario)
			guardarAlumnos.append(nombreAppend.getFullNameCintaEdad())
			print(nombreAppend.getFullNameCintaEdad())
		camposNecesarios()	
		start()
	

	elif preguntaQueHacer == '2':
		for printAlumnos in guardarAlumnos:
			print(printAlumnos)
		start()	

start()

