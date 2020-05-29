from model.model import Model
from view.view import View

class Controller:
    """
    *********************************************************
    * Controlador de la base de datos de la venta de tickets*
    *********************************************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.menu_sesion()
    
    """
    ************************************************
    *             Controles Generales              *
    ************************************************
    """
    def menu_sesion(self):
        while 1: 
            self.view.menu_sesion()
            self.view.preguntar('Usuario: ')
            usuario = input()
            self.view.preguntar('Contraseña: ')
            contraseña = input()
            admin = self.model.leer_usuario_contraseña(usuario, contraseña)
            if type(admin) == tuple:
                print('Bienvenido/a ' + usuario)
                if admin[0] == 'Si':
                    self.menu_admin(usuario)
                elif admin[0] == 'No':
                    self.menu_general(usuario)
            else:
                if admin == None:
                    self.view.error('Credenciales incorrectas')
                else:
                    self.view.error('Problema al leer el usuario, revise')
        return

    def menu_general(self, usuario):
        opcion = '0'
        while opcion != '5':
            self.view.menu_general()
            self.view.opcion('5')
            opcion = input()
            if opcion == '1':
                self.agregar_ticket(usuario)
            elif opcion == '2':
                self.leer_todo_horarios_disponibles()
            elif opcion == '3':
                self.leer_horario_pelicula()
            elif opcion == '4':
                self.leer_horario_dia()
            elif opcion == '5':
                self.view.end()
                return
            else: 
                self.view.opcion_invalida()
        return

    def menu_admin(self, usuario):
        opcion = '0'
        while opcion != '10':
            self.view.menu_admin()
            self.view.opcion('10')
            opcion = input()
            if opcion == '1':
                self.agregar_ticket(usuario)
            elif opcion == '2':
                self.leer_todo_horarios_disponibles()
            elif opcion == '3':
                self.menu_peliculas()
            elif opcion == '4':
                self.menu_horarios()
            elif opcion == '5':
                self.menu_usuarios()
            elif opcion == '6':
                self.menu_salas()
            elif opcion == '7':
                self.menu_asientos()
            elif opcion == '8':
                self.menu_salas_asientos()
            elif opcion == '9':
                self.menu_tickets()
            elif opcion == '10':
                self.view.end()
                return
            else: 
                self.view.opcion_invalida()
        return

    def actualizar_listas(self, fs, vs):
        campos = []
        valores = []
        for f, v in zip(fs,vs):
            if v != '':
                campos.append(f+' = %s')
                valores.append(v)
        return campos, valores


    """
    ************************************************
    *            Controles de peliculas            *
    ************************************************
    """
    def menu_peliculas(self):
        opcion = '0'
        while opcion != '6':
            self.view.menu_peliculas()
            self.view.opcion('6')
            opcion = input()
            if opcion == '1':
                self.leer_todo_peliculas()
            elif opcion == '2':
                self.leer_id_peliculas()
            elif opcion == '3':
                self.agregar_pelicula()
            elif opcion == '4':
                self.actualizar_pelicula()
            elif opcion == '5':
                self.borrar_pelicula()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_pelicula(self):
        self.view.preguntar('Titulo: ')
        titulo = input()
        self.view.preguntar('Descripcion: ')
        descripcion = input()
        self.view.preguntar('Duracion(minutos): ')
        duracion = input()
        self.view.preguntar('Idioma(Ingles/Español): ')
        idioma = input()
        self.view.preguntar('Subtitulos(Ingles/Español/No): ')
        subtitulos = input()
        self.view.preguntar('Clasificacion(AA/A/B/B-15/C/D): ')
        clasificacion = input()
        self.view.preguntar('Precio(Pesos): ')
        precio = input()
        return [titulo, descripcion, duracion, idioma, subtitulos, clasificacion, precio]
    
    def leer_id_peliculas(self):
        self.view.preguntar('ID: ')
        i_id = input()
        pelicula = self.model.leer_id_peliculas(i_id)
        if type(pelicula) == tuple:
            self.view.mostrar_cabecera_pelicula(' Datos de la pelicula '+i_id+' ')
            self.view.mostrar_pelicula(pelicula)
            self.view.mostrar_separador_pelicula()
            self.view.mostrar_pie_pelicula()
        else:
            if pelicula == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la pelicula, revise')
        return

    def leer_todo_peliculas(self):
        peliculas = self.model.leer_todo_peliculas()
        if type(peliculas) == list:
            self.view.mostrar_cabecera_pelicula(' Todas las Peliculas ')
            for pelicula in peliculas:
                self.view.mostrar_pelicula(pelicula)
                self.view.mostrar_separador_pelicula()
            self.view.mostrar_pie_pelicula()
        else:
            self.view.error('Problema al leer las peliculas, revise')
        return

    def agregar_pelicula(self):
        self.view.preguntar("ID: ")
        ID = input()
        titulo, descripcion, duracion, idioma, subtitulos, clasificacion, precio = self.pregunta_pelicula()
        salida = self.model.agregar_pelicula(ID, titulo, descripcion, duracion, idioma, subtitulos, clasificacion, precio)
        if salida == True:
            self.view.Ok(titulo, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('La pelicula esta repetida.')
            else:
                self.view.error('No se pudo agregar la pelicula, revise.')
        return
    
    def actualizar_pelicula(self):
        self.view.preguntar('ID de la pelicula a modificar: ')
        i_ID = input()
        ID = self.model.leer_id_peliculas(i_ID)
        if type(ID) == tuple:
            self.view.mostrar_cabecera_pelicula(' Datos de la pelicula '+ i_ID+' ')
            self.view.mostrar_pelicula(ID)
            self.view.mostrar_separador_pelicula()
            self.view.mostrar_pie_pelicula()
        else:
            if  ID == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer el ID, revise')
            return
        self.view.mensaje('Ingresa los valores a modificar (Vacio para dejarlo igual): ')
        todos_valores = self.pregunta_pelicula()
        campos, valores = self.actualizar_listas(['titulo', 'descripcion', 'duracion', 'idioma', 'subtitulos', 'clasificacion', 'precio_pelicula'], todos_valores)
        valores.append(i_ID)
        valores = tuple(valores)
        salida = self.model.actualizar_pelicula(campos, valores)
        if salida == True:
            self.view.Ok(i_ID, 'Actualizo')
        else:
            self.view.error('No se pudo actualizar el ID, Revise.')
        return 

    def borrar_pelicula(self):
        self.view.preguntar('ID de la pelicula a borrar: ')
        i_ID = input()
        count = self.model.borrar_pelicula(i_ID)
        if count != 0:
            self.view.Ok(i_ID, 'Borro')
        else:
            if count == 0:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer el codigo, revise.')


    """
    ************************************************
    *            Controles de Usuarios             *
    ************************************************
    """
    def menu_usuarios(self):
        opcion = '0'
        while opcion != '6':
            self.view.menu_usuarios()
            self.view.opcion('6')
            opcion = input()
            if opcion == '1':
                self.leer_todo_usuarios()
            elif opcion == '2':
                self.leer_username_usuarios()
            elif opcion == '3':
                self.agregar_usuario()
            elif opcion == '4':
                self.actualizar_usuario()
            elif opcion == '5':
                self.borrar_usuario()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_usuario(self):
        self.view.preguntar('Nombre de usuario: ')
        username = input()
        self.view.preguntar('Nombre: ')
        nombre = input()
        self.view.preguntar('Apellido Paterno: ')
        apellido_pat = input()
        self.view.preguntar('Apellido Materno: ')
        apellido_mat = input()
        self.view.preguntar('Contraseña: ')
        contraseña = input()
        self.view.preguntar('Administrador?(Si/No): ')
        admin = input()
        return [username, nombre, apellido_pat, apellido_mat, contraseña, admin]
    
    def pregunta_usuario_act(self):
        self.view.preguntar('Nombre: ')
        nombre = input()
        self.view.preguntar('Apellido Paterno: ')
        apellido_pat = input()
        self.view.preguntar('Apellido Materno: ')
        apellido_mat = input()
        self.view.preguntar('Contraseña: ')
        contraseña = input()
        self.view.preguntar('Administrador?(Si/No): ')
        admin = input()
        return [nombre, apellido_pat, apellido_mat, contraseña, admin]
    
    def leer_todo_usuarios(self):
        usuarios = self.model.leer_todo_usuarios()
        if type(usuarios) == list:
            self.view.mostrar_cabecera_usuario(' Todos los Usuarios ')
            for usuario in usuarios:
                self.view.mostrar_usuario(usuario)
                self.view.mostrar_separador_usuario()
            self.view.mostrar_pie_usuario()
        else:
            self.view.error('Problema al leer el usuario, revise')
        return
    
    def leer_username_usuarios(self):
        self.view.preguntar('Nombre de usuario: ')
        username = input()
        usuario = self.model.leer_username_usuarios(username)
        if type(usuario) == tuple:
            self.view.mostrar_cabecera_usuario(' Datos del usuario '+username+' ')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_separador_usuario()
            self.view.mostrar_pie_usuario()
        else:
            if usuario == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al leer el usuario, revise')
        return

    def agregar_usuario(self):
        username, nombre, apellido_pat, apellido_mat, contraseña, admin = self.pregunta_usuario()
        salida = self.model.agregar_usuario(username, nombre, apellido_pat, apellido_mat, contraseña, admin)
        if salida == True:
            self.view.Ok(username, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('El usuario ya existe.')
            else:
                self.view.error('No se pudo agregar el usuario, revise.')
        return

    def actualizar_usuario(self):
        self.view.preguntar('Nombre de usuario a modificar: ')
        i_username = input()
        usuario = self.model.leer_username_usuarios(i_username)
        if type(usuario) == tuple:
            self.view.mostrar_cabecera_usuario(' Datos de '+ i_username +' ')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_separador_usuario()
            self.view.mostrar_pie_usuario()
        else:
            if  usuario == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al leer el nombre de usuario, revise')
            return
        self.view.mensaje('Ingresa los valores a modificar (Vacio para dejarlo igual): ')
        todos_valores = self.pregunta_usuario_act()
        campos, valores = self.actualizar_listas(['nombre', 'apellido_pat', 'apellido_mat', 'contraseña', 'admin'], todos_valores)
        valores.append(i_username)
        valores = tuple(valores)
        salida = self.model.actualizar_usuario(campos, valores)
        if salida == True:
            self.view.Ok(i_username, 'Actualizo')
        else:
            self.view.error('No se pudo actualizar el usuario, Revise.')
        return 

    def borrar_usuario(self):
        self.view.preguntar('Nombre de usuario de la pelicula a borrar: ')
        i_username = input()
        count = self.model.borrar_usuario(i_username)
        if count != 0:
            self.view.Ok(i_username, 'Borro')
        else:
            if count == 0:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al borrar el usuario, revise.')


    """
    ************************************************
    *            Controles de Asientos             *
    ************************************************
    """
    def menu_asientos(self):
        opcion = '0'
        while opcion != '6':
            self.view.menu_asientos()
            self.view.opcion('6')
            opcion = input()
            if opcion == '1':
                self.leer_todo_asientos()
            elif opcion == '2':
                self.leer_id_asiento()
            elif opcion == '3':
                self.agregar_asiento()
            elif opcion == '4':
                self.actualizar_asiento()
            elif opcion == '5':
                self.borrar_asiento()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return
    
    def pregunta_asiento(self):
        self.view.preguntar('Categoria: ')
        categoria = input()
        return [categoria]
    
    def leer_todo_asientos(self):
        asientos = self.model.leer_todo_asientos()
        if type(asientos) == list:
            self.view.mostrar_cabecera_asiento(' Todos los Asientos ')
            for asiento in asientos:
                self.view.mostrar_asiento(asiento)
                self.view.mostrar_separador_asiento()
            self.view.mostrar_pie_asiento()
        else:
            self.view.error('Problema al leer el asiento, revise')
        return

    def leer_id_asiento(self):
        self.view.preguntar('Id del tipo de asiento: ')
        i_asiento_id = input()
        asiento = self.model.leer_id_asiento(i_asiento_id)
        if type(asiento) == tuple:
            self.view.mostrar_cabecera_asiento(' Datos del asiento '+ i_asiento_id +' ')
            self.view.mostrar_asiento(asiento)
            self.view.mostrar_separador_asiento()
            self.view.mostrar_pie_asiento()
        else:
            if asiento == None:
                self.view.error('El tipo de asiento no existe')
            else:
                self.view.error('Problema al leer el tipo de asiento, revise')
        return
    
    def agregar_asiento(self):
        self.view.preguntar("ID: ")
        ID = input() 
        self.view.preguntar("Categoria: ")
        categoria = input()
        salida = self.model.agregar_asiento(ID, categoria)
        if salida == True:
            self.view.Ok(ID, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('El tipo de asiento ya existe.')
            else:
                self.view.error('No se pudo agregar el tipo de asiento, revise.')
        return

    def actualizar_asiento(self):
        self.view.preguntar('ID del asiento a modificar: ')
        i_asiento_id = input()
        asiento = self.model.leer_id_asiento(i_asiento_id)
        if type(asiento) == tuple:
            self.view.mostrar_cabecera_asiento(' Datos de '+ i_asiento_id +' ')
            self.view.mostrar_asiento(asiento)
            self.view.mostrar_separador_asiento()
            self.view.mostrar_pie_asiento()
        else:
            if  asiento == None:
                self.view.error('El asiento no existe')
            else:
                self.view.error('Problema al leer el ID del tipo de asiento, revise')
            return
        self.view.mensaje('Ingresa los valores a modificar (Vacio para dejarlo igual): ')
        todos_valores = self.pregunta_asiento()
        campos, valores = self.actualizar_listas(['categoria'], todos_valores)
        valores.append(i_asiento_id)
        valores = tuple(valores)
        salida = self.model.actualizar_asiento(campos, valores)
        if salida == True:
            self.view.Ok(i_asiento_id, 'Actualizo')
        else:
            self.view.error('No se pudo actualizar el tipo de asiento, Revise.')
        return 

    def borrar_asiento(self):
        self.view.preguntar('ID del tipo de asiento a borrar: ')
        i_asiento_id = input()
        count = self.model.borrar_asiento(i_asiento_id)
        if count != 0:
            self.view.Ok(i_asiento_id, 'Borro')
        else:
            if count == 0:
                self.view.error('El tipo de asiento no existe')
            else:
                self.view.error('Problema al borrar el tipo de asiento, revise.')
    
    """
    ************************************************
    *             Controles de Salas               *
    ************************************************
    """
    def menu_salas(self):
        opcion = '0'
        while opcion != '6':
            self.view.menu_salas()
            self.view.opcion('6')
            opcion = input()
            if opcion == '1':
                self.leer_todo_salas()
            elif opcion == '2':
                self.leer_numero_sala()
            elif opcion == '3':
                self.agregar_sala()
            elif opcion == '4':
                self.actualizar_sala()
            elif opcion == '5':
                self.borrar_sala()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return
    
    def pregunta_sala(self):
        self.view.preguntar('Tipo de sala: ')
        tipo = input()
        self.view.preguntar('Descripcion: ')
        descripcion = input()
        self.view.preguntar('Precio de sala(Pesos): ')
        precio_sala = input()
        return [tipo, descripcion, precio_sala]
    
    def leer_todo_salas(self):
        salas = self.model.leer_todo_salas()
        if type(salas) == list:
            self.view.mostrar_cabecera_sala(' Todos las salas ')
            for sala in salas:
                self.view.mostrar_sala(sala)
                self.view.mostrar_separador_sala()
            self.view.mostrar_pie_sala()
        else:
            self.view.error('Problema al leer la informacion de la sala, revise')
        return

    def leer_numero_sala(self):
        self.view.preguntar('Numero de la sala: ')
        i_numero_sala = input()
        sala = self.model.leer_numero_sala(i_numero_sala)
        if type(sala) == tuple:
            self.view.mostrar_cabecera_sala(' Datos del asiento '+ i_numero_sala +' ')
            self.view.mostrar_sala(sala)
            self.view.mostrar_separador_sala()
            self.view.mostrar_pie_sala()
        else:
            if sala == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al leer la informacion de la sala, revise')
        return
    
    def agregar_sala(self):
        self.view.preguntar("Numero de sala: ")
        numero_sala = input() 
        tipo, descripcion, precio_sala = self.pregunta_sala()
        salida = self.model.agregar_sala(numero_sala, tipo, descripcion, precio_sala)
        if salida == True:
            self.view.Ok(numero_sala, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('El numero de sala ya existe.')
            else:
                self.view.error('No se pudo agregar la sala, revise.')
        return

    def actualizar_sala(self):
        self.view.preguntar('Numero de la sala a modificar: ')
        i_numero_sala = input()
        sala = self.model.leer_numero_sala(i_numero_sala)
        if type(sala) == tuple:
            self.view.mostrar_cabecera_sala(' Datos de '+ i_numero_sala +' ')
            self.view.mostrar_sala(sala)
            self.view.mostrar_separador_sala()
            self.view.mostrar_pie_sala()
        else:
            if  sala == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al leer la informacion de la sala, revise')
            return
        self.view.mensaje('Ingresa los valores a modificar (Vacio para dejarlo igual): ')
        todos_valores = self.pregunta_sala()
        campos, valores = self.actualizar_listas(['tipo', 'descripcion', 'precio_sala'], todos_valores)
        valores.append(i_numero_sala)
        valores = tuple(valores)
        salida = self.model.actualizar_sala(campos, valores)
        if salida == True:
            self.view.Ok(i_numero_sala, 'Actualizo')
        else:
            self.view.error('No se pudo actualizar la informacion de la sala, Revise.')
        return 

    def borrar_sala(self):
        self.view.preguntar('Numero de la sala a borrar: ')
        i_numero_sala = input()
        count = self.model.borrar_sala(i_numero_sala)
        if count != 0:
            self.view.Ok(i_numero_sala, 'Borro')
        else:
            if count == 0:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al borrar la sala, revise.')
            
    """
    ************************************************
    *         Controles de Salas_Asientos          *
    ************************************************
    """
    def menu_salas_asientos(self):
        opcion = '0'
        while opcion != '6':
            self.view.menu_salas_asientos()
            self.view.opcion('6')
            opcion = input()
            if opcion == '1':
                self.leer_asientos_salas()
            elif opcion == '2':
                self.leer_sala_asiento()
            elif opcion == '3':
                self.agregar_asiento_sala()
            elif opcion == '4':
                self.borrar_asiento_sala()
            elif opcion == '5':
                self.actualizar_cantidad_asientos()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return
    
    def leer_asientos_salas(self):
        self.view.preguntar('Numero de la sala: ')
        i_numero_sala = input()
        asientos = self.model.leer_asientos_sala(i_numero_sala)
        if type(asientos) == list:
            self.view.mostrar_cabecera_sala_asiento(' Todos los asientos ')
            for asiento in asientos:
                self.view.mostrar_asientos_sala(asiento)
                self.view.mostrar_separador_sala_asiento()
            self.view.mostrar_pie_sala_asiento()
        else:
            self.view.error('Problema al leer la informacion de la sala, revise')
        return
    
    def leer_asientos_cantidad(self, i_numero_sala):
        cantidad = self.model.leer_asientos_cantidad(i_numero_sala)
        total = 0
        if type(cantidad) == list:
            for tipo in cantidad:
                total += tipo[0]
            return total
        else:
            self.view.error('Problema de cantidad, revise')
        return

    def leer_sala_asiento(self):
        self.view.preguntar('ID del asiento: ')
        i_id_asiento = input()
        salas = self.model.leer_sala_asiento(i_id_asiento)
        if type(salas) == list:
            self.view.mostrar_cabecera_sala_asiento(' Todas las salas ')
            for sala in salas:
                self.view.mostrar_sala_asiento(sala)
                self.view.mostrar_separador_sala_asiento()
            self.view.mostrar_pie_sala_asiento()
        else:
            self.view.error('Problema al leer la informacion del asiento, revise')
        return
    
    def agregar_asiento_sala(self):
        self.view.preguntar("A que sala quiere agregar el nuevo tipo de asiento: ")
        i_numero_sala = input()
        self.view.preguntar("Que tipo de asiento desea agregar: ")
        i_id_asiento = input()
        self.view.preguntar("Cuantos asientos desea agregar: ")
        i_cantidad = input()
        salida = self.model.agregar_asiento_sala(i_numero_sala, i_id_asiento, i_cantidad)
        if salida == True:
            self.view.Ok(i_id_asiento, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('La sala ya cuenta con ese tipo de asientos.')
            else:
                self.view.error('No se pudo agregar el tipo de asiento, revise.')
        return
    
    def borrar_asiento_sala(self):
        self.view.preguntar('Numero de la sala: ')
        i_numero_sala = input()
        self.view.preguntar('Tipo de asiento: ')
        i_asiento_id = input()
        count = self.model.borrar_asiento_sala(i_numero_sala, i_asiento_id)
        if count != 0:
            self.view.Ok(i_asiento_id, 'Borro')
        else:
            if count == 0:
                self.view.error('La sala no tiene ese tipo de asiento')
            else:
                self.view.error('Problema al borrar el tipo de asiento, revise.')
    
    def actualizar_cantidad_asientos(self):
        self.view.preguntar("Que sala? : ")
        i_numero_sala = input()
        self.view.preguntar("Que tipo de asiento?: ")
        i_id_asiento = input()
        self.view.preguntar("Cuantos asientos tendra ahora: ")
        i_cantidad = input()
        salida = self.model.actualizar_cantidad_asientos(i_numero_sala, i_id_asiento, i_cantidad)
        if salida == True:
            self.view.Ok(i_numero_sala, 'modifico')
        else:
            if salida.errno == 1062:
                self.view.error('La sala no tiene ese tipo de asientos.')
            else:
                self.view.error('No se pudo modificar el tipo de asiento, revise.')
        return

    """
    ************************************************
    *            Controles de Horarios             *
    ************************************************
    """
    
    def menu_horarios(self):
        opcion = '0'
        while opcion != '6':
            self.view.menu_horarios()
            self.view.opcion('6')
            opcion = input()
            if opcion == '1':
                self.leer_todo_horarios_disponibles()
            elif opcion == '2':
                self.leer_todo_horarios_no_disponibles()
            elif opcion == '3':
                self.agregar_horario()
            elif opcion == '4':
                self.actualizar_actualizar_horario()
            elif opcion == '5':
                self.borrar_horario()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_horario(self):
        self.view.preguntar("ID de la pelicula: ")
        h_pelicula_id = input()
        self.view.preguntar("Numero de sala: ")
        h_numero_sala = input()
        self.view.preguntar("Ya termino la pelicula?(Si/No): ")
        terminado = input()
        return [h_pelicula_id, h_numero_sala, terminado]

    def leer_todo_horarios_disponibles(self):
        horarios = self.model.leer_todo_horarios_disponibles()
        if type(horarios) == list:
            self.view.mostrar_cabecera_sala(' Todos los horarios disponibles: ')
            for horario in horarios:
                self.view.mostrar_horario(horario)
                self.view.mostrar_separador_horario()
            self.view.mostrar_pie_horario()
        else:
            self.view.error('Problema al leer la informacion del horario, revise')
        return
    
    def leer_todo_horarios_no_disponibles(self):
        horarios = self.model.leer_todo_horarios_no_disponibles()
        if type(horarios) == list:
            self.view.mostrar_cabecera_sala(' Todos los horarios no disponibles: ')
            for horario in horarios:
                self.view.mostrar_horario(horario)
                self.view.mostrar_separador_horario()
            self.view.mostrar_pie_horario()
        else:
            self.view.error('Problema al leer la informacion del horario, revise')
        return

    def leer_horario_pelicula(self):
        self.view.preguntar("ID de la pelicula: ")
        i_pelicula_id = input()
        horarios = self.model.leer_horario_pelicula(i_pelicula_id)
        if type(horarios) == list:
            self.view.mostrar_cabecera_sala('Todos los horarios disponibles: ')
            for horario in horarios:
                self.view.mostrar_horario(horario)
                self.view.mostrar_separador_horario()
            self.view.mostrar_pie_horario()
        else:
            self.view.error('Problema al leer la informacion del horario, revise')
        return

    def leer_horario_dia(self):
        self.view.preguntar('Dia? (formato DD): ')
        dia = input()
        self.view.preguntar('Mes? (formato MM): ')
        mes = input()
        self.view.preguntar('Año?(formato YYYY): ')
        año = input()
        fecha_hora_inicial = año + '-' + mes + '-' + dia + ' ' + ':00:00' + ':00'
        dia = int(dia) + 1
        dia = str(dia)
        fecha_hora_final = año + '-' + mes + '-' + dia + ' ' + ':00:00' + ':00'
        horarios = self.model.leer_horario_dia(fecha_hora_inicial, fecha_hora_final)
        if type(horarios) == list:
            self.view.mostrar_cabecera_sala('Todos los horarios disponibles: ')
            for horario in horarios:
                self.view.mostrar_horario(horario)
                self.view.mostrar_separador_horario()
            self.view.mostrar_pie_horario()
        else:
            self.view.error('Problema al leer la informacion del horario, revise')
        return

    def agregar_horario(self):
        self.view.preguntar('ID de la pelicula?: ')
        h_pelicula_id = input()
        self.view.preguntar('Numero de la sala: ')
        h_numero_sala = input()
        self.view.preguntar('Dia? (formato DD): ')
        dia = input()
        self.view.preguntar('Mes? (formato MM): ')
        mes = input()
        self.view.preguntar('Año?(formato YYYY): ')
        año = input()
        self.view.preguntar('Hora?(formato hh:mm): ')
        hora = input()
        fecha_hora = año + '-' + mes + '-' + dia + ' ' + hora + ':00'
        asientos_disponibles = self.leer_asientos_cantidad(h_numero_sala)
        terminado = 'No'
        salida = self.model.agregar_horario(h_pelicula_id, h_numero_sala, fecha_hora, asientos_disponibles, terminado)
        if salida == True:
            self.view.Ok(h_pelicula_id, 'agrego')
        else:
            self.view.error('No se pudo agregar el horario, revise.')
        return
        
    def actualizar_actualizar_horario(self):
        self.view.preguntar('ID del horario a modificar ')
        horario_id = input()
        horario = self.model.leer_id_horario(horario_id)
        if type(horario) == tuple:
            self.view.mostrar_cabecera_horario(' Datos de '+ horario_id +' ')
            self.view.mostrar_horario(horario)
            self.view.mostrar_separador_horario()
            self.view.mostrar_pie_horario()
        else:
            if  horario == None:
                self.view.error('El horario no existe')
            else:
                self.view.error('Problema al leer la informacion del horario, revise')
            return
        self.view.mensaje('Ingresa los valores a modificar (Vacio para dejarlo igual): ')
        todos_valores = self.pregunta_horario()
        campos, valores = self.actualizar_listas(['h_pelicula_id', 'h_numero_sala', 'terminado'], todos_valores)
        valores.append(horario_id)
        valores = tuple(valores)
        salida = self.model.actualizar_horario(campos, valores)
        if salida == True:
            self.view.Ok(horario_id, 'Actualizo')
        else:
            self.view.error('No se pudo actualizar la informacion del horario, Revise.')
        return 

    def borrar_horario(self):
        self.view.preguntar('ID del horario a borrar: ')
        horario_id = input()
        count = self.model.borrar_horario(horario_id)
        if count != 0:
            self.view.Ok(horario_id, 'Borro')
        else:
            if count == 0:
                self.view.error('El horario no existe')
            else:
                self.view.error('Problema al borrar el horario, revise.')

    """
    ************************************************
    *             Controles de Tickets             *
    ************************************************
    """

    def menu_tickets(self):
        opcion = '0'
        while opcion != '4':
            self.view.menu_tickets()
            self.view.opcion('4')
            opcion = input()
            if opcion == '1':
                self.mostrar_todo_tickets()
            elif opcion == '2':
                self.mostrar_usuario_tickets()
            elif opcion == '3':
                self.mostrar_horario_tickets()
            elif opcion == '4':
                return
            else: 
                self.view.opcion_invalida()
        return

    def mostrar_todo_tickets(self):
        tickets = self.model.mostrar_todo_tickets()
        if type(tickets) == list:
            self.view.mostrar_cabecera_pelicula(' Todos los tickets ')
            for ticket in tickets:
                self.view.mostrar_ticket(ticket)
                self.view.mostrar_separador_ticket()
            self.view.mostrar_pie_ticket()
        else:
            self.view.error('Problema al leer los tickets, revise')
        return

    def mostrar_usuario_tickets(self):
        self.view.preguntar('Que nombre de usuario?: ')
        i_username = input()
        tickets = self.model.mostrar_usuario_tickets(i_username)
        if type(tickets) == list:
            self.view.mostrar_cabecera_pelicula(' Todas los tickets de usuario ')
            for ticket in tickets:
                self.view.mostrar_ticket(ticket)
                self.view.mostrar_separador_ticket()
            self.view.mostrar_pie_ticket()
        else:
            self.view.error('Problema al leer los tickets, revise')
        return
    
    def mostrar_horario_tickets(self):
        self.view.preguntar('ID del horario: ')
        i_ID = input()
        tickets = self.model.mostrar_horario_tickets(i_ID)
        if type(tickets) == list:
            self.view.mostrar_cabecera_pelicula(' Todos los tickets del horario ')
            for ticket in tickets:
                self.view.mostrar_ticket(ticket)
                self.view.mostrar_separador_ticket()
            self.view.mostrar_pie_ticket()
        else:
            self.view.error('Problema al leer los tickets, revise')
        return

    def agregar_ticket(self, i_username):
        self.view.preguntar("ID del horario: ")
        i_horario_id = input()
        if self.model.leer_disponible_horario(i_horario_id) == 1:
            if self.model.asiento_disponible(i_horario_id) == 1:
                precio_ticket = self.model.obtener_precio_ticket(i_horario_id)
                salida = self.model.agregar_ticket(i_username, i_horario_id, precio_ticket)
                if salida == True:
                    self.view.Ok(i_horario_id, 'agrego')
                    self.model.reducir_asiento(i_horario_id)
                    print("================================Datos del ticket================================")
                    horario = self.model.leer_id_horario_ticket(i_horario_id)
                    print('Vendedor: ' + i_username)
                    print('Precio: ' + str(precio_ticket) + ' Pesos')
                    self.view.mostrar_horario_ticket(horario)
                    self.view.mostrar_separador_horario()
                    self.view.mostrar_pie_horario()
                else:
                    self.view.error('No se pudo agregar el ticket, revise.')
                return
            elif self.model.asiento_disponible(i_horario_id) == 0:
                print('========== No hay asiento disponible ==========')
        elif self.model.leer_disponible_horario(i_horario_id) == 0:
            print('=========== Horario no disponible, intente de nuevo ===========')
        else:
            self.view.error('El horario no existe.')
        return
        
        
        