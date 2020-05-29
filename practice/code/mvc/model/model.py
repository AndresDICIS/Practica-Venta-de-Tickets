from mysql import connector

class Model:
    """
    *******************************************************
    * Modelo para la base de datos de la venta de tickets *
    *******************************************************
    """

    def __init__(self, config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    
    def read_config_db(self):
        d = {}
        with open(self.config_db_file,) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()


    """
    **********************
    *      Peliculas     *
    **********************
    """

    def leer_todo_peliculas(self):
        try:
            consulta_sql = 'SELECT * FROM peliculas'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    
    def leer_id_peliculas(self, ID):
        try:
            consulta_sql = 'SELECT * FROM peliculas WHERE pelicula_id = %s'
            valores = (ID,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def agregar_pelicula(self, ID, titulo, descripcion, duracion, idioma, subtitulos, clasificacion, precio):
        try:
            consulta_sql = 'INSERT INTO peliculas (`pelicula_id`, `titulo`, `descripcion`, `duracion`, `idioma`, `subtitulos`, `clasificacion`, `precio_pelicula`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            valores = (ID, titulo, descripcion, duracion, idioma, subtitulos, clasificacion, precio)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def actualizar_pelicula(self, campos, valores):
        try:
            consulta_sql = 'UPDATE peliculas SET '+','.join(campos)+' WHERE pelicula_id = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_pelicula(self, ID):
        try:
            consulta_sql = 'DELETE FROM peliculas WHERE pelicula_id = %s'
            valores = (ID,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    """
    **********************
    *      Usuarios      *
    **********************
    """

    def leer_todo_usuarios(self):
        try:
            consulta_sql = 'SELECT * FROM usuarios'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_username_usuarios(self, username):
        try:
            consulta_sql = 'SELECT * FROM usuarios WHERE username = %s'
            valores = (username,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def leer_usuario_contraseña(self, username, contraseña):
        try:
            consulta_sql = 'SELECT admin FROM usuarios WHERE username = %s AND contraseña = %s'
            valores = (username,contraseña)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def agregar_usuario(self, username, nombre, apellido_pat, apellido_mat, contraseña, admin):
        try:
            consulta_sql = 'INSERT INTO usuarios (`username`, `nombre`, `apellido_pat`, `apellido_mat`, `contraseña`, `admin`) VALUES (%s, %s, %s, %s, %s, %s)'
            valores = (username, nombre, apellido_pat, apellido_mat, contraseña, admin)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def actualizar_usuario(self, campos, valores):
        try:
            consulta_sql = 'UPDATE usuarios SET '+','.join(campos)+' WHERE username = %s'  
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_usuario(self, username):
        try:
            consulta_sql = 'DELETE FROM usuarios WHERE username = %s'
            valores = (username,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **********************
    *      Asientos      *
    **********************
    """

    def leer_todo_asientos(self):
        try:
            consulta_sql = 'SELECT * FROM asientos'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_id_asiento(self, ID):
        try:
            consulta_sql = 'SELECT * FROM asientos WHERE asiento_id = %s'
            valores = (ID,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def leer_asientos_cantidad(self, numero_sala):
        try:
            consulta_sql = 'SELECT cantidad FROM sala_asiento WHERE sa_numero_sala = %s'
            valores = (numero_sala,)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def agregar_asiento(self, ID, categoria):
        try:
            consulta_sql = 'INSERT INTO asientos (`asiento_id`, `categoria`) VALUES (%s, %s)'
            valores = (ID, categoria)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def actualizar_asiento(self, campos, valores):
        try:
            consulta_sql = 'UPDATE asientos SET '+','.join(campos)+' WHERE asiento_id = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_asiento(self, ID):
        try:
            consulta_sql = 'DELETE FROM asientos WHERE asiento_id = %s'
            valores = (ID,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **********************
    *        Salas       *
    **********************
    """

    def leer_todo_salas(self):
        try:
            consulta_sql = 'SELECT * FROM salas'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    
    def leer_numero_sala(self, numero_sala):
        try:
            consulta_sql = 'SELECT * FROM salas WHERE numero_sala = %s'
            valores = (numero_sala,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def agregar_sala(self, numero_sala, tipo, descripcion, precio_sala):
        try:
            consulta_sql = 'INSERT INTO salas (`numero_sala`, `tipo`, `descripcion`, `precio_sala`) VALUES (%s, %s, %s, %s)'
            valores = (numero_sala, tipo, descripcion, precio_sala)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def actualizar_sala(self, campos, valores):
        try:
            consulta_sql = 'UPDATE salas SET '+','.join(campos)+' WHERE numero_sala = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_sala(self, numero):
        try:
            consulta_sql = 'DELETE FROM salas WHERE numero_sala = %s'
            valores = (numero,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **********************
    *   Salas-Asientos   *
    **********************
    """

    def leer_asientos_sala(self, numero_sala):
        try:
            consulta_sql = 'SELECT A.asiento_id, A.categoria, SA.cantidad FROM asientos A, sala_asiento SA WHERE SA.sa_numero_sala = %s AND SA.sa_asiento_id = A.asiento_id'
            valores = (numero_sala,)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def leer_sala_asiento(self, asiento_id):
        try:
            consulta_sql = 'SELECT S.numero_sala, S.tipo, S.descripcion, S.precio_sala FROM sala_asiento SA ,salas S WHERE SA.sa_asiento_id = %s AND SA.sa_numero_sala = S.numero_sala'
            valores = (asiento_id,)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def agregar_asiento_sala(self, numero_sala, id_asiento, cantidad):
        try:
            consulta_sql = 'INSERT INTO sala_asiento (`sa_numero_sala`, `sa_asiento_id`, `cantidad`) VALUES (%s, %s, %s)'
            valores = (numero_sala, id_asiento, cantidad)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def borrar_asiento_sala(self, numero_sala, asiento_id):
        try:
            consulta_sql = 'DELETE FROM sala_asiento WHERE sa_numero_sala = %s AND sa_asiento_id = %s'
            valores = (numero_sala, asiento_id)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
            
    def actualizar_cantidad_asientos(self, i_numero_sala, i_id_asiento, i_cantidad):
        try:
            consulta_sql = 'UPDATE sala_asiento SET cantidad = %s WHERE sa_numero_sala = %s AND sa_asiento_id = %s'
            valores = (i_cantidad, i_numero_sala, i_id_asiento)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    """
    **********************
    *      Horarios      *
    **********************
    """
    def leer_id_horario(self, ID):
        try:
            consulta_sql = 'SELECT H.horario_id, P.titulo, H.h_numero_sala, H.fecha_hora, H.asientos_disponibles FROM horario H, peliculas P WHERE P.pelicula_id = H.h_pelicula_id AND H.horario_id = %s'
            valores = (ID,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def leer_id_horario_ticket(self, ID):
        try:
            consulta_sql = 'SELECT P.titulo, H.h_numero_sala, H.fecha_hora FROM horario H, peliculas P WHERE P.pelicula_id = H.h_pelicula_id AND H.horario_id = %s'
            valores = (ID,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def leer_todo_horarios_disponibles(self):
        try:
            consulta_sql = 'SELECT H.horario_id, P.titulo, H.h_numero_sala, H.fecha_hora, H.asientos_disponibles FROM horario H, peliculas P WHERE P.pelicula_id = H.h_pelicula_id AND H.terminado = \'No\''
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def leer_horario_pelicula(self, id_pelicula):
        try:
            consulta_sql = 'SELECT H.horario_id, P.titulo, H.h_numero_sala, H.fecha_hora, H.asientos_disponibles FROM horario H, peliculas P WHERE P.pelicula_id = H.h_pelicula_id AND H.h_pelicula_id = %s AND H.terminado = \'No\''
            valores = (id_pelicula,)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    
    def leer_horario_dia(self, fecha_hora_inicial, fecha_hora_final):
        try:
            consulta_sql = 'SELECT H.horario_id, P.titulo, H.h_numero_sala, H.fecha_hora, H.asientos_disponibles FROM horario H, peliculas P WHERE H.terminado = \'No\' AND P.pelicula_id = H.h_pelicula_id AND H.fecha_hora BETWEEN %s AND %s'
            valores = (fecha_hora_inicial, fecha_hora_final)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def leer_todo_horarios_no_disponibles(self):
        try:
            consulta_sql = 'SELECT H.horario_id, P.titulo, H.h_numero_sala, H.fecha_hora, H.asientos_disponibles FROM horario H, peliculas P WHERE P.pelicula_id = H.h_pelicula_id AND H.terminado = \'Si\''
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    
    def agregar_horario(self, h_pelicula_id, h_numero_sala, fecha_hora, asientos_disponibles, terminado):
        try:
            consulta_sql = 'INSERT INTO horario(`h_pelicula_id`, `h_numero_sala`, `fecha_hora`, `asientos_disponibles`, `terminado`) VALUES(%s, %s, %s, %s, %s);'
            valores = (h_pelicula_id, h_numero_sala, fecha_hora, asientos_disponibles, terminado)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def actualizar_horario(self, campos, valores):
        try:
            consulta_sql = 'UPDATE horario SET '+','.join(campos)+' WHERE horario_id = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_horario(self, ID):
        try:
            consulta_sql = 'DELETE FROM horario WHERE horario_id = %s'
            valores = (ID,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    """
    **********************
    *      tickets       *
    **********************
    """

    def mostrar_todo_tickets(self):
        try:
            consulta_sql = 'SELECT T.ticket_id, U.username, P.pelicula_id, H.fecha_hora, T.precio_ticket FROM tickets T, peliculas P, horario H, usuarios U WHERE U.username = T.t_username AND P.pelicula_id = H.h_pelicula_id AND H.horario_id = T.t_horario_id'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    
    def mostrar_usuario_tickets(self, i_username):
        try:
            consulta_sql = 'SELECT T.ticket_id, U.username, P.pelicula_id, H.fecha_hora, T.precio_ticket FROM tickets T, peliculas P, horario H, usuarios U WHERE T.t_username = %s AND U.username = T.t_username AND P.pelicula_id = H.h_pelicula_id AND H.horario_id = T.t_horario_id'
            valor = (i_username, )
            self.cursor.execute(consulta_sql, valor)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def mostrar_horario_tickets(self, i_horario_id):
        try:
            consulta_sql = 'SELECT T.ticket_id, U.username, P.pelicula_id, H.fecha_hora, T.precio_ticket FROM tickets T, peliculas P, horario H, usuarios U WHERE T.t_horario_id = %s AND U.username = T.t_username AND P.pelicula_id = H.h_pelicula_id AND H.horario_id = T.t_horario_id'
            valor = (i_horario_id, )
            self.cursor.execute(consulta_sql, valor)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    def obtener_precio_ticket(self, horario_id):
        try:
            total = 0
            consulta_sql_sala = 'SELECT S.precio_sala FROM salas S, horario H WHERE S.numero_sala = H.h_numero_sala AND H.horario_id = %s'
            consulta_sql_pelicula = 'SELECT P.precio_pelicula FROM peliculas P, horario H WHERE P.pelicula_id = H.h_pelicula_id AND H.horario_id = %s'
            valor = (horario_id,)
            self.cursor.execute(consulta_sql_sala, valor)
            record = self.cursor.fetchone()
            total += record[0]
            self.cursor.execute(consulta_sql_pelicula, valor)
            record = self.cursor.fetchone()
            total += record[0]
            return total
        except connector.Error as err:
            return err 

    def leer_disponible_horario(self, i_horario_id):
        try:
            consulta_sql = 'SELECT terminado FROM horario WHERE horario_id = %s'
            valor = (i_horario_id,)
            self.cursor.execute(consulta_sql, valor)
            record = self.cursor.fetchone()
            if record == None:
                return record
            else:
                if record[0] == 'No':
                    return 1
                elif record[0] == 'Si':
                    return 0
        except connector.Error as err:
            return err 

    def agregar_ticket(self, i_username, i_horario_id, precio_ticket):
        try:
            consulta_sql = 'INSERT INTO tickets (`t_username`, `t_horario_id`, `precio_ticket`) VALUES (%s, %s, %s)'
            valores = (i_username, i_horario_id, precio_ticket)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def asiento_disponible(self, i_horario_id):
        try:
            consulta_sql = 'SELECT asientos_disponibles FROM horario WHERE horario_id = %s'
            valor = (i_horario_id,)
            self.cursor.execute(consulta_sql, valor)
            record = self.cursor.fetchone()
            if record == None:
                return record
            else:
                if record[0] > 0:
                    return 1
                elif record[0] <= 0:
                    return 0
        except connector.Error as err:
            return err

    def reducir_asiento(self, i_horario_id):
        try:
            consulta_sql = 'SELECT asientos_disponibles FROM horario WHERE horario_id = %s'
            valor = (i_horario_id,)
            self.cursor.execute(consulta_sql, valor)
            record = self.cursor.fetchone()
            asientos = record[0]
            asientos = asientos - 1
            consulta_sql = 'UPDATE horario SET asientos_disponibles = %s WHERE horario_id = %s '
            valor = (asientos, i_horario_id)
            self.cursor.execute(consulta_sql, valor)
            self.cnx.commit()
        except:
            self.cnx.rollback()
