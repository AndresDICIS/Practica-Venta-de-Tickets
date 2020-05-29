class View:
    """
    ******************************************
    * Vista para base de datos de Cine *
    ******************************************
    """

    def start(self):
        print("===========================================")
        print("=Bienvenido al Sistema de Tickets de Cine.=")
        print("===========================================")

    def end(self):
        print("======================================")
        print("=        Sistema cerrado             =")
        print("======================================")
    
    def menu_sesion(self):
        print("======================================")
        print("=          Inicio de Sesion          =")
        print("======================================")

    def menu_admin(self):
        print("======================================")
        print("=       Menu de Administrador        =")
        print("======================================")
        print('1.- Generar un Ticket')
        print('2.- Ver horarios')
        print('3.- Peliculas')
        print('4.- Horarios')
        print('5.- Usuarios')
        print('6.- Salas')
        print('7.- Asientos')
        print('8.- Relacion de las salas y los asientos')
        print('9.- Tickets')
        print('10.- Salir')
    
    def menu_general(self):
        print("======================================")
        print("=            Menu General            =")
        print("======================================")
        print('1.- Generar un Ticket')
        print('2.- Ver horarios')
        print('3.- Ver horarios por pelicula')
        print('4.- Ver horarios por dia')
        print('5.- Salir')

    
    def preguntar(self, output):
        print(output, end = '')

    def opcion(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def opcion_invalida(self):
        print('¡Opcion no valida!\nIntente de nuevo')
    
    def Ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+ str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def mensaje(self, output):
        print(output)
    
    def error(self, err):
        print(' ¡Error! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
 
    """
    Menu Peliculas
    """

    def menu_peliculas(self):
        print("======================================")
        print("=          Menu de Peliculas         =")
        print("======================================")
        print('1.- Ver lista de peliculas')
        print('2.- Ver pelicula por ID')
        print('3.- Agregar nueva pelicula')
        print('4.- Actualizar pelicula')
        print('5.- Borrar pelicula')
        print('6.- Regresar')

    def mostrar_pelicula(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Descripcion: ', record[2])
        print('Duracion(minutos): ', record[3])
        print('Idioma: ', record[4])
        print('Subtitulos: ', record[5])
        print('Clasificacion: ', record[6])
        print('Precio: ', record[7])
    
    def mostrar_cabecera_pelicula(self, header):
        print(header.center(80, '*'))
        print('-'*80)

    def mostrar_separador_pelicula(self):
        print('-'*80)

    def mostrar_pie_pelicula(self):
        print('*'*80)
    
    """
    Menu Usuarios
    """

    def menu_usuarios(self):
        print("======================================")
        print("=          Menu de Usuarios          =")
        print("======================================")
        print('1.- Ver lista de usuarios')
        print('2.- Ver informacion por nombre de usuario')
        print('3.- Agregar nuevo usuario')
        print('4.- Actualizar usuario')
        print('5.- Borrar usuario')
        print('6.- Regresar')

    def mostrar_usuario(self, record):
        print('Nombre de usuario: ', record[0])
        print('Nombre: ', record[1] + ' ' + record[2] + ' ' + record[3])
        print('Contraseña: ', record[4])
        print('Es administrador: ', record[5])
    
    def mostrar_cabecera_usuario(self, header):
        print(header.center(100, '*'))
        print('-'*100)

    def mostrar_separador_usuario(self):
        print('-'*100)

    def mostrar_pie_usuario(self):
        print('*'*100)
    

    """
    Menu Asientos
    """

    def menu_asientos(self):
        print("======================================")
        print("=          Menu de Asientos          =")
        print("======================================")
        print('1.- Ver todos los tipos de asientos')
        print('2.- Ver informacion de asiento por ID')
        print('3.- Agregar nuevo tipo de asiento')
        print('4.- Actualizar tipo de asiento')
        print('5.- Borrar tipo de asiento')
        print('6.- Regresar')

    def mostrar_asiento(self, record):
        print('ID de asiento: ', record[0])
        print('Categoria: ', record[1])

    def mostrar_cabecera_asiento(self, header):
        print(header.center(60, '*'))
        print('-'*60)

    def mostrar_separador_asiento(self):
        print('-'*60)

    def mostrar_pie_asiento(self):
        print('*'*60)
    

    """
    Menu Salas
    """

    def menu_salas(self):
        print("======================================")
        print("=            Menu de Salas           =")
        print("======================================")
        print('1.- Ver todos las salas')
        print('2.- Ver informacion de sala por numero')
        print('3.- Agregar nuevo tipo de sala')
        print('4.- Actualizar tipo de Sala')
        print('5.- Borrar tipo de Sala')
        print('6.- Regresar')

    def mostrar_sala(self, record):
        print('Numero de sala: ', record[0])
        print('Tipo de sala: ', record[1])
        print('Descripcion: ', record[2])
        print('Precio: ', record[3])

    def mostrar_cabecera_sala(self, header):
        print(header.center(100, '*'))
        print('-'*100)

    def mostrar_separador_sala(self):
        print('-'*100)

    def mostrar_pie_sala(self):
        print('*'*100)
    

    """
    Menu Salas_Asientos
    """

    def menu_salas_asientos(self):
        print("======================================")
        print("=       Menu de Salas_Asientos       =")
        print("======================================")
        print('1.- Ver todos los asientos de una sala')
        print('2.- Ver las salas que tiene cierto tipo de asiento')
        print('3.- Agregar tipos de asientos a una sala')
        print('4.- Quitar tipos de asientos a una sala')
        print('5.- Modificar el numero de asientos de una sala')
        print('6.- Regresar')

    def mostrar_asientos_sala(self, record):
        print('ID de Asiento: ', record[0])
        print('Categoria de Asiento: ', record[1])
        print('Cantidad de Asientos: ', record[2])
    
    def mostrar_sala_asiento(self, record):
        print('Sala numero: ', record[0])
        print('Tipo: ', record[1])
        print('Descripcion: ', record[2])
        print('Precio: ', record[3])

    def mostrar_cabecera_sala_asiento(self, header):
        print(header.center(100, '*'))
        print('-'*100)

    def mostrar_separador_sala_asiento(self):
        print('-'*100)

    def mostrar_pie_sala_asiento(self):
        print('*'*100)


    """
    Menu Horario
    """

    def menu_horarios(self):
        print("======================================")
        print("=          Menu de Horarios          =")
        print("======================================")
        print('1.- Mostrar horarios disponibles')
        print('2.- Mostrar horarios no disponibles')
        print('3.- Agregar un horario')
        print('4.- Modificar un horario')
        print('5.- Borrar un horario')
        print('6.- Regresar')

    def mostrar_horario(self, record):
        print('ID: ', record[0])
        print('Pelicula: ', record[1])
        print('Numero de Sala: ', record[2])
        print('Fecha y hora: ', record[3])
        print('Asientos disponibles: ', record[4])

    def mostrar_horario_ticket(self, record):
        print('Pelicula: ', record[0])
        print('Numero de Sala: ', record[1])
        print('Fecha y hora: ', record[2])

    def mostrar_cabecera_horario(self, header):
        print(header.center(100, '*'))
        print('-'*100)

    def mostrar_separador_horario(self):
        print('-'*100)

    def mostrar_pie_horario(self):
        print('*'*100)

    """
    Menu tickets
    """

    def menu_tickets(self):
        print("======================================")
        print("=          Menu de Tickets           =")
        print("======================================")
        print('1.- Mostrar todos los tickets')
        print('2.- Mostrar tickets por usuario')
        print('3.- Mostrar tickets por horario')
        print('4.- Regresar')

    def mostrar_ticket(self, record):
        print('Numero de ticket: ', record[0])
        print('Usuario: ', record[1])
        print('Pelicula ', record[2])
        print('Fecha y hora: ', record[3])
        print('Precio ', record[4])
    
    def mostrar_cabecera_ticket(self, header):
        print(header.center(100, '*'))
        print('-'*100)

    def mostrar_separador_ticket(self):
        print('-'*100)

    def mostrar_pie_ticket(self):
        print('*'*100)
