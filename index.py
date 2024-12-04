import customtkinter
from PIL import Image
import sqlite3
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk

class App(customtkinter.CTk):
      
      def __init__(self):
        super().__init__()

        self.title("Cantina") 
        self.geometry("1200x720") 
        self.resizable(False,False)
        self.iconbitmap("icono.ico")

        customtkinter.set_appearance_mode("dark") 
        
        self.lift() 
        self.focus_force()  

        self.beige = "#c69c6d"
        self.blanco = "#000000"
        self.naranja = "#ffa36c"
        self.blanco = "#FEFEFF"
        self.verde = "#00FF00"  
        self.rojo = "#FF0000"   
        self.gris = "#5F5F5F"
        self.negro="#000000"
        self.naranja_oscuro ="#BB794E"
        self.gris_oscuro="#404040"
        self.gris_ultra_oscuro="#242424"
        self.marron="#573F1D"
        self.fuente_h1 = "Optima"
        self.tamaño_h1 = 20
        self.tamaño_h2 = 15

        

        self.mostrar_logo()
        self.mostrar_login()
      
      def mostrar_logo(self):
        self.logo_frame = customtkinter.CTkFrame(self)
        self.logo_frame.pack(pady=20, 
                             padx=20)

        logo_image = customtkinter.CTkImage(Image.open("img/banner.png"), 
                                            size=(1200, 320))
        self.logo_label = customtkinter.CTkLabel(self.logo_frame, 
                                                 image=logo_image, 
                                                 text="")
        self.logo_label.pack()

      def mostrar_login(self):
        
        if hasattr(self, 'register_frame'):
            self.register_frame.pack_forget()
            self.mostrar_logo()


        self.login_frame = customtkinter.CTkFrame(self, 
                                                  fg_color=self.gris_oscuro)
        self.login_frame.pack(pady=0, 
                              padx=20, 
                              fill="both", 
                              expand=True)
    

        self.correo_label = customtkinter.CTkLabel(self.login_frame, 
                                                   text="Correo electrónico", 
                                                   text_color=self.blanco, 
                                                   font=(self.fuente_h1, self.tamaño_h1))
        self.correo_label.pack(pady=16, 
                               padx=(0, 135))
        self.correo_entry = customtkinter.CTkEntry(self.login_frame, 
                                                   placeholder_text="Introduzca su correo electrónico", 
                                                   width=300)
        self.correo_entry.pack(pady=0, 
                               padx=0)

        self.contraseña_label = customtkinter.CTkLabel(self.login_frame, 
                                                       text="Contraseña", 
                                                       text_color=self.blanco, 
                                                       font=(self.fuente_h1, 
                                                             self.tamaño_h1))
        self.contraseña_label.pack(pady=16, 
                                   padx=(0, 190))
        self.contraseña_entry = customtkinter.CTkEntry(self.login_frame, 
                                                       placeholder_text="Introduzca su contraseña", 
                                                       width=300, 
                                                       show="*")
        self.contraseña_entry.pack(pady=0, 
                                   padx=0)

        self.iniciar_sesion_button = customtkinter.CTkButton(self.login_frame, 
                                                             text="Iniciar sesión",
                                                             hover_color= self.naranja_oscuro,
                                                             font=(self.fuente_h1, 
                                                                   self.tamaño_h2), 
                                                             fg_color=self.naranja, 
                                                             text_color=self.blanco,
                                                             command=self.iniciar_sesion)
        self.iniciar_sesion_button.pack(pady=26, 
                                        padx=0)

        self.registrarse_button = customtkinter.CTkButton(self.login_frame, 
                                                          text="Registrarse", 
                                                          hover_color= self.naranja_oscuro, 
                                                          font=(self.fuente_h1, 
                                                                self.tamaño_h2), 
                                                          fg_color=self.naranja, 
                                                          text_color=self.blanco, 
                                                          command=self.mostrar_registro)
        self.registrarse_button.pack(pady=0, 
                                     padx=0)

      def mostrar_registro(self):

        self.login_frame.pack_forget()
        self.logo_frame.pack_forget()

        self.register_frame = customtkinter.CTkFrame(self,
                                                     fg_color=self.gris_oscuro)
        self.register_frame.pack(pady=20, 
                                 padx=20, 
                                 fill="both", 
                                 expand=True)

        self.registro_label = customtkinter.CTkLabel(self.register_frame,
                                                     text="Formulario de Registro",
                                                     font=(self.fuente_h1, 
                                                           28),
                                                     text_color=self.blanco)
        self.registro_label.pack(pady=80)

        self.nombre_label = customtkinter.CTkLabel(self.register_frame,
                                                   text="Nombre",
                                                   font=(self.fuente_h1,
                                                         self.tamaño_h1),
                                                   text_color=self.blanco)
        self.nombre_label.pack(pady=5, 
                               padx=(0,220))
        self.nombre_entry = customtkinter.CTkEntry(self.register_frame,
                                                   placeholder_text="Nombre",
                                                   width=300)
        self.nombre_entry.pack(pady=10)

        self.apellido_label = customtkinter.CTkLabel(self.register_frame,
                                                     text="Apellido",
                                                     font=(self.fuente_h1,
                                                           self.tamaño_h1),
                                                     text_color=self.blanco)
        self.apellido_label.pack(pady=5,
                                 padx=(0,220))
        self.apellido_entry = customtkinter.CTkEntry(self.register_frame,
                                                     placeholder_text="Apellido",
                                                     width=300)
        self.apellido_entry.pack(pady=10)

        self.email_label = customtkinter.CTkLabel(self.register_frame,
                                                  text="Correo electrónico",
                                                  font=(self.fuente_h1, 
                                                        self.tamaño_h1),
                                                  text_color=self.blanco)
        self.email_label.pack(pady=5,
                              padx=(0,130))
        self.email_entry = customtkinter.CTkEntry(self.register_frame,
                                                  placeholder_text="Correo electrónico",
                                                  width=300)
        self.email_entry.pack(pady=10)

        self.password_label = customtkinter.CTkLabel(self.register_frame, 
                                                     text="Contraseña", 
                                                     font=(self.fuente_h1, 
                                                           self.tamaño_h1), 
                                                           text_color=self.blanco)
        self.password_label.pack(pady=5,
                                 padx=(0,190))
        self.password_entry = customtkinter.CTkEntry(self.register_frame,
                                                     placeholder_text="Contraseña",
                                                     show="*",
                                                     width=300)
        self.password_entry.pack(pady=10)

        self.crear_cuenta_button = customtkinter.CTkButton(self.register_frame, 
                                                           text="Crear cuenta",
                                                           hover_color= self.naranja_oscuro, 
                                                           font=(self.fuente_h1, 
                                                                 self.tamaño_h2), 
                                                           fg_color=self.naranja, 
                                                           text_color=self.gris_oscuro,
                                                           command=self.crear_usuario)
        self.crear_cuenta_button.pack(pady=20)

        volver_image = customtkinter.CTkImage(Image.open("img/flecha.png"),
                                              size=(20,20))
        self.volver_button = customtkinter.CTkButton(self.register_frame,
                                                     text="",
                                                     fg_color=self.naranja,
                                                     hover_color=self.naranja_oscuro,
                                                     image=volver_image, width=5,
                                                     command=self.mostrar_login)
        self.volver_button.place(y=20, x=20)
      
      def mostrar_cantina(self):

        self.cantina_frame = customtkinter.CTkFrame(self,bg_color=self.gris_oscuro,width=1250,height=750)
        self.cantina_frame.pack(pady=40, 
                                padx=40)

        cantina_image = customtkinter.CTkImage(Image.open("img/plano.png"),
                                               size=(1120,640))
        self.logo_label = customtkinter.CTkLabel(self.cantina_frame, 
                                                image=cantina_image, 
                                                text="",
                                                bg_color=self.gris_oscuro)
        self.logo_label.pack()

        self.login_frame.pack_forget()
        self.logo_frame.pack_forget()

        self.reservar_frame = customtkinter.CTkFrame(self)
        self.reservar_frame.pack(pady=20,
                                 padx=20)
         
        self.panel_admin_button=customtkinter.CTkButton(self.cantina_frame,
                                                           text="Panel admin ⚙️ ",
                                                           font=(self.fuente_h1,25),
                                                           text_color="#4B6E91",
                                                           corner_radius=20,
                                                           border_width=1,
                                                           fg_color=self.blanco,
                                                           border_color="#4B6E91",
                                                           bg_color="#D9D9D9",
                                                           width=200,
                                                           height=25,
                                                           command=self.panel_admin)
        self.panel_admin_button.place(x=6,y=480)    

        self.mi_reserva_button=customtkinter.CTkButton(self.cantina_frame,
                                                           text="Mi reserva 📆",
                                                           font=(self.fuente_h1,25),
                                                           text_color="#4B6E91",
                                                           corner_radius=20,
                                                           border_width=1,
                                                           fg_color=self.blanco,
                                                           border_color="#4B6E91",
                                                           bg_color="#D9D9D9",
                                                           width=200,
                                                           height=25,
                                                           command=self.mi_reserva)
        self.mi_reserva_button.place(x=6,y=535)

        self.cerrar_sesion_button=customtkinter.CTkButton(self.cantina_frame,
                                                           text="Cerrar sesión 🔒",
                                                           font=(self.fuente_h1,25),
                                                           text_color="#4B6E91",
                                                           corner_radius=25,
                                                           border_width=1,
                                                           fg_color=self.blanco,
                                                           hover_color="red",
                                                           border_color="#4B6E91",
                                                           bg_color="#C2BFBF",
                                                           width=25,
                                                           height=25,
                                                           command=self.cerrar_sesion)
        self.cerrar_sesion_button.place(y=590,x=6)
        
        #boton 1 silla redonda blanca 
        
        self.sitio1_button=customtkinter.CTkButton(self.cantina_frame,text="1",
                                                   text_color=self.negro,
                                                   font=(self.fuente_h1, 
                                                   self.tamaño_h1),corner_radius=30,
                                                   fg_color=self.blanco,
                                                   border_color=self.negro,
                                                   bg_color="#C2BFBF",
                                                   border_width=1,
                                                   width=70,
                                                   height=70,
                                                   command=lambda: self.reservar(1))
        self.sitio1_button.place(x=220,
                                 y=50)

        #boton 2  silla redonda blanca
        self.sitio2_button=customtkinter.CTkButton(self.cantina_frame,
                                                   text="2",
                                                   text_color=self.negro,
                                                   font=(self.fuente_h1,self.tamaño_h1),
                                                   corner_radius=30,
                                                   fg_color=self.blanco,
                                                   border_color=self.negro,
                                                   bg_color="#C2BFBF",
                                                   border_width=1,
                                                   width=70,
                                                   height=70,
                                                   command=lambda: self.reservar(2))
        self.sitio2_button.place(x=80,
                                 y=200)

        #boton 3  silla redonda blanca 
        self.sitio3_button=customtkinter.CTkButton(self.cantina_frame,
                                                   text="3",
                                                   text_color=self.negro,
                                                   font=(self.fuente_h1, self.tamaño_h1),
                                                   corner_radius=30,
                                                   fg_color=self.blanco,
                                                   border_color=self.negro,
                                                   bg_color="#C2BFBF",
                                                   border_width=1,
                                                   width=70,
                                                   height=70,
                                                   command=lambda: self.reservar(3))
        self.sitio3_button.place(x=990,
                                 y=310)

        #boton 4 silla 1
        self.sitio4_button=customtkinter.CTkButton(self.cantina_frame,
                                                   text="4",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1,self.tamaño_h1),
                                                   fg_color=self.marron,
                                                   border_color=self.negro,
                                                   border_width=1,
                                                   width=80,
                                                   height=100,
                                                   command=lambda: self.reservar(4))
        self.sitio4_button.place(x=755,
                                 y=40)
        

        #boton 5 silla 2 marron
        self.sitio5_button=customtkinter.CTkButton(self.cantina_frame,
                                                   text="5",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1,self.tamaño_h1),
                                                   fg_color=self.marron,
                                                   border_color=self.negro,
                                                   border_width=1,
                                                   width=80,
                                                   height=100,
                                                   command=lambda: self.reservar(5))
        self.sitio5_button.place(x=755,
                                 y=170)

        #boton 6 silla 3 marron
        self.sitio6_button=customtkinter.CTkButton(self.cantina_frame,
                                                   text="6",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1, 
                                                   self.tamaño_h1),
                                                   fg_color=self.marron,
                                                   border_color=self.negro,
                                                   border_width=1,
                                                   width=80,
                                                   height=100,
                                                   command=lambda: self.reservar(6))
        self.sitio6_button.place(x=405,
                                 y=40)

        #boton 7 silla 4 marron
        self.sitio7_button=customtkinter.CTkButton(self.cantina_frame,text="7",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1,
                                                   self.tamaño_h1),
                                                   fg_color=self.marron,
                                                   border_color=self.negro,
                                                   border_width=1,
                                                   width=80,
                                                   height=100,
                                                   command=lambda: self.reservar(7))
        self.sitio7_button.place(x=405,
                                 y=173) 

      def reservar(self,silla_id):
        self.popup = customtkinter.CTkToplevel(self)
        self.popup.title("Reservar")
        self.popup.resizable(False, False)
        self.popup.configure(fg_color=self.gris_oscuro)

        window_width = 300
        window_height = 250
        screen_width = self.winfo_width()
        screen_height = self.winfo_height()
        position_x = self.winfo_x() + (screen_width // 2) - (window_width // 2)
        position_y = self.winfo_y() + (screen_height // 2) - (window_height // 2)

        self.popup.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.silla_seleccionada = silla_id


        self.reservar_detalle = customtkinter.CTkFrame(self.popup,
                                                fg_color=self.gris_oscuro)
        self.reservar_detalle.pack(pady=20,
                                  padx=20,
                                  fill="both",
                                  expand=True)
        
        self.horas_label=customtkinter.CTkLabel(self.reservar_detalle,
                                                text="Horas",
                                                text_color=self.blanco,
                                                font=(self.fuente_h1,
                                                      self.tamaño_h1))
        self.horas_label.pack(pady=20,
                              padx=20)
        
        self.horas_entry=customtkinter.CTkOptionMenu(self.reservar_detalle,
                                                     fg_color=self.gris,
                                                     text_color=self.blanco,
                                                     button_color=self.naranja,
                                                     button_hover_color=self.naranja_oscuro,
                                                     values=["13:30 - 14:00",
                                                             "14:00 - 14:30",
                                                             "14:30 - 15:00",
                                                             "15:00 - 15:30"])
        self.horas_entry.pack(pady=0,
                              padx=0)

        self.aceptar_reserva_button=customtkinter.CTkButton(self.reservar_detalle,
                                                            text="Aceptar reserva",
                                                            text_color=self.blanco,
                                                            font=(self.fuente_h1,
                                                                  self.tamaño_h2),
                                                            fg_color=self.naranja,
                                                            hover_color=self.naranja_oscuro,
                                                            command=self.crear_reserva)
        self.aceptar_reserva_button.pack(pady=20,
                                         padx=0)

      def panel_admin(self):
            try:
                  self.admin_popup = customtkinter.CTkToplevel(self)
                  self.admin_popup.title("Panel de Administración")
                  self.admin_popup.geometry("800x600")
                  self.admin_popup.configure(fg_color=self.gris_oscuro)

                  self.admin_frame = customtkinter.CTkFrame(self.admin_popup, fg_color=self.gris_oscuro)
                  self.admin_frame.pack(fill="both", expand=True, padx=20, pady=20)

                  self.label_admin = customtkinter.CTkLabel(
                        self.admin_frame,
                        text="Usuarios Registrados",
                        text_color=self.blanco,
                        font=(self.fuente_h1, self.tamaño_h1)
                  )
                  self.label_admin.pack(pady=10)

                  self.tree_frame = customtkinter.CTkFrame(self.admin_frame, fg_color=self.gris_oscuro)
                  self.tree_frame.pack(fill="both", expand=True)

                  self.tree = ttk.Treeview(
                        self.tree_frame,
                        columns=("ID", "Nombre", "Apellido", "Correo"),
                        show="headings",
                        height=15
                  )

                  self.tree.heading("ID", text="ID")
                  self.tree.heading("Nombre", text="Nombre")
                  self.tree.heading("Apellido", text="Apellido")
                  self.tree.heading("Correo", text="Correo Electrónico")

                  self.tree.column("ID", width=50, anchor="center")
                  self.tree.column("Nombre", width=150, anchor="center")
                  self.tree.column("Apellido", width=150, anchor="center")
                  self.tree.column("Correo", width=200, anchor="center")

                  self.tree.pack(fill="both", expand=True)

                  self.actualizar_tabla()

                  self.eliminar_button = customtkinter.CTkButton(
                        self.admin_frame,
                        text="Eliminar Usuario",
                        text_color=self.blanco,
                        font=(self.fuente_h1, self.tamaño_h2),
                        fg_color=self.rojo,
                        hover_color=self.naranja_oscuro,
                        command=self.eliminar_usuario_seleccionado
                  )
                  self.eliminar_button.pack(pady=20)

            except Exception as e:
                  self.centrar_messagebox("error", "Error inesperado", f"Se produjo un error: {str(e)}")


      def mi_reserva(self):
            try:
                  if not self.obtener_reserva_usuario():  # Esto obtiene `self.hora_actual`
                        return

                  self.popup = customtkinter.CTkToplevel(self)
                  self.popup.title("Modificar Reserva")
                  self.popup.resizable(False, False)
                  self.popup.configure(fg_color=self.gris_oscuro)

                  window_width = 300
                  window_height = 300
                  screen_width = self.winfo_width()
                  screen_height = self.winfo_height()
                  position_x = self.winfo_x() + (screen_width // 2) - (window_width // 2)
                  position_y = self.winfo_y() + (screen_height // 2) - (window_height // 2)

                  self.popup.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

                  self.modificar_frame = customtkinter.CTkFrame(self.popup, fg_color=self.gris_oscuro)
                  self.modificar_frame.pack(pady=20, padx=20, fill="both", expand=True)

                  self.horas_label = customtkinter.CTkLabel(
                        self.modificar_frame,
                        text="Nuevo Horario",
                        text_color=self.blanco,
                        font=(self.fuente_h1, self.tamaño_h1)
                  )
                  self.horas_label.pack(pady=10, padx=10)

                  opciones_horas = ["13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30"]

                  self.horas_entry = customtkinter.CTkOptionMenu(
                        self.modificar_frame,
                        fg_color=self.gris,
                        text_color=self.blanco,
                        button_color=self.naranja,
                        button_hover_color=self.naranja_oscuro,
                        values=opciones_horas
                  )

                  if self.hora_actual in opciones_horas:  # Usa la hora obtenida de la reserva
                        self.horas_entry.set(self.hora_actual)

                  self.horas_entry.pack(pady=10, padx=10)

                  self.aceptar_modificacion_button = customtkinter.CTkButton(
                        self.modificar_frame,
                        text="Guardar Cambios",
                        text_color=self.blanco,
                        font=(self.fuente_h1, self.tamaño_h2),
                        fg_color=self.naranja,
                        hover_color=self.naranja_oscuro,
                        command=self.confirmar_modificar_reserva
                  )
                  self.aceptar_modificacion_button.pack(pady=20, padx=20)

            except sqlite3.Error as e:
                  self.centrar_messagebox("error", "Error de base de datos", f"Se produjo un error al mostrar la ventana: {str(e)}")
            except Exception as e:
                  self.centrar_messagebox("error", "Error inesperado", f"Se produjo un error {str(e)}")

      def crear_usuario(self):
            try:
                  nombre=self.nombre_entry.get()
                  apellido=self.apellido_entry.get()
                  email=self.email_entry.get()
                  password=self.password_entry.get()

                  conn=sqlite3.connect("cantina_db.db") # Indicamos la ruta donde queremos conectarnos
                  cursor=conn.cursor() #inicializar una conexión

                  cursor.execute("INSERT INTO usuarios (nombre,apellido,correo_electronico,contraseña) VALUES (?,?,?,?)",(nombre,apellido,email,password)) #consulta de SQL
                  conn.commit() # confirmar la conexión
                  self.centrar_messagebox("info", "Registro completado", "Enhorabuena tu registro ha sido completado")
                  self.register_frame.pack_forget()
                  self.mostrar_login()
                  return True # significa para indicarle que salio todo bien la inserccion de datos
            except sqlite3.IntegrityError: 
                  return False #Significa para indicarle que salio todo mal!!!

      def crear_reserva(self):
            try:
                  self.fecha = datetime.now().strftime("%Y-%m-%d")
                  self.hora = self.horas_entry.get() 

                  if not self.usuario_id or not self.hora or not self.silla_seleccionada:
                        self.centrar_messagebox("Error", "Error", "Faltan datos para realizar la reserva.")
                        return

                  conn = sqlite3.connect("cantina_db.db")
                  cursor = conn.cursor()

                  cursor.execute(
                        "SELECT * FROM reservas WHERE fecha = ? AND hora = ? AND silla = ?",
                        (self.fecha, self.hora, self.silla_seleccionada)
                  )
                  resultado = cursor.fetchone()

                  if resultado:
                        self.centrar_messagebox("warning", "Cuidado", f"La silla {self.silla_seleccionada} ya está reservada en el horario {self.hora}.")
                        return

                  cursor.execute(
                        "INSERT INTO reservas (id_usuario, fecha, hora, silla) VALUES (?, ?, ?, ?)",
                        (self.usuario_id, self.fecha, self.hora, self.silla_seleccionada)
                  )
                  conn.commit()

                  self.centrar_messagebox("info", "Èxito", "La reserva fue realizada correctamente.")
                  self.popup.destroy()
                  self.mostrar_cantina()
            except sqlite3.Error as e:
                  self.centrar_messagebox("error", "Error de base de datos", f"Se produjo un error en la base de datos: {str(e)}")
            except Exception as e:
                  self.centrar_messagebox("error", "Error inesperado", f"Se produjo un error: {str(e)}")
            finally:
                  if conn:
                        conn.close()

      def obtener_reserva_usuario(self):
            try:
                  conn = sqlite3.connect("cantina_db.db")
                  cursor = conn.cursor()

                  cursor.execute(
                        "SELECT id, silla, hora FROM reservas WHERE id_usuario = ? AND fecha = ?",
                        (self.usuario_id, datetime.now().strftime("%Y-%m-%d"))
                  )
                  resultado = cursor.fetchone()

                  if resultado:
                        self.reserva_id = resultado[0]
                        self.silla_seleccionada = resultado[1]
                        self.hora_actual = resultado[2]
                        return True
                  else:
                        self.centrar_messagebox("warning", "Sin reservas", "No tiene reservas en el día de hoy")
                        return False

                  self.centrar_messagebox("error", "Error de base", f"Error al obtener la reserva: {str(e)}")                 
                  return False
            finally:
                  if conn:
                        conn.close()
            
      def confirmar_modificar_reserva(self):
            try:
                  self.hora = self.horas_entry.get()
                  self.fecha = datetime.now().strftime("%Y-%m-%d")

                  if not self.hora:
                        self.centrar_messagebox("error", "Error", "Debe seleccionar un horario.")
                        return

                  conn = sqlite3.connect("cantina_db.db")
                  cursor = conn.cursor()

                  cursor.execute(
                        "SELECT * FROM reservas WHERE fecha = ? AND hora = ? AND silla = ? AND id != ?",
                        (self.fecha, self.hora, self.silla_seleccionada, self.reserva_id),
                  )
                  resultado = cursor.fetchone()

                  if resultado:
                        self.centrar_messagebox("warning", "Conflicto de reserva", f"La silla {self.silla_seleccionada} ya está reservada en el horario {self.hora}.")
                        return
                  else:
                        cursor.execute(
                              "UPDATE reservas SET hora = ? WHERE id = ?",
                              (self.hora, self.reserva_id)
                        )
                        conn.commit()

                  if conn.total_changes == 0:
                        self.centrar_messagebox("error", "Error", "No se realizó ninguna modificación. Verifique los datos.")
                        return

                  self.centrar_messagebox("info", "Éxito", "La reserva fue modificada correctamente")
                  self.popup.destroy()
                  self.mostrar_cantina()
            except sqlite3.Error as e:
                  self.centrar_messagebox("error", "Error en la base de datos",  f"Se produjo un error en la base de datos: {str(e)}")
            except Exception as e:
                  self.centrar_messagebox("error", "Error inesperado", f"Se produjo un error: {str(e)}")
            finally:
                  if conn:
                        conn.close()

      def eliminar_reservar(self):
            try:
                  conn=sqlite3.connect("cantina_db.db") # Indicamos la ruta donde queremos conectarnos
                  cursor=conn.cursor #inicializar una conexión
                  
                  cursor.execute("DELETE FROM reservas WHERE id = ?")
                  conn.commit()
                  
                  return True
            except sqlite3.Integrity.Error:
                  return False  

      def actualizar_tabla(self):
            try:
                  conn = sqlite3.connect("cantina_db.db")
                  cursor = conn.cursor()
                  cursor.execute("SELECT id, nombre, apellido, correo_electronico FROM usuarios")
                  usuarios = cursor.fetchall()

                  for row in self.tree.get_children():
                        self.tree.delete(row)

                  for usuario in usuarios:
                        self.tree.insert("", "end", values=usuario)

            except sqlite3.Error as e:
                  self.centrar_messagebox("error", "Error en la base de datos", f"Error al cargar usuarios: {str(e)}")
            finally:
                  if conn:
                        conn.close()

      def eliminar_usuario_seleccionado(self):
            try:
                  selected_item = self.tree.selection()
                  if not selected_item:
                        self.centrar_messagebox("warning", "Selección Vacía", "Por favor, selecciona un usuario para eliminar.")
                        return

                  usuario = self.tree.item(selected_item)["values"]
                  usuario_id = usuario[0]

                  confirm = self.centrar_messagebox("yesno", "Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar al usuario con ID {usuario_id}?")
                  if not confirm:
                        return

                  conn = sqlite3.connect("cantina_db.db")
                  cursor = conn.cursor()
                  cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
                  conn.commit()
                                    
                  self.centrar_messagebox("info", "Usuario Eliminado", f"El usuario con ID {usuario_id} ha sido eliminado.")
                  self.actualizar_tabla()

            except sqlite3.Error as e:
                  self.centrar_messagebox("error", "Error de base de datos", f"Error al eliminar el usuario: {str(e)}")
            finally:
                  if conn:
                        conn.close()

      def iniciar_sesion(self):
            try:
                  email = self.correo_entry.get()
                  contraseña = self.contraseña_entry.get()

                  if not email or not contraseña:
                        self.centrar_messagebox("warning", "Error de entrada", "Por favor, complete todos los campos.")
                        return

                  conn = sqlite3.connect("cantina_db.db")
                  cursor = conn.cursor()

                  cursor.execute("SELECT id FROM usuarios WHERE correo_electronico = ? AND contraseña = ?", (email, contraseña))
                  resultado = cursor.fetchone()

                  if resultado:
                        self.usuario_id = resultado[0]  # Guarda el ID del usuario

                        cursor.execute("SELECT id FROM reservas WHERE id_usuario = ?", (self.usuario_id,))
                        reserva = cursor.fetchone()

                        if reserva:
                              self.reserva_id = reserva[0]  # Guarda el ID de la reserva
                        else:
                              self.reserva_id = None

                        self.login_frame.pack_forget()
                        self.mostrar_cantina()
                  else:
                        self.centrar_messagebox("warning", "Error", "Las credenciales introducidas son incorrectas.")
            except sqlite3.Error as e:
                  self.centrar_messagebox("error", "Error en la base de datos", f"Se produjo un error en la base de datos: {str(e)}")
            except Exception as e:
                  self.centrar_messagebox("error", "Error inesperado", f"Se produjo un error: {str(e)}")

            finally:
                  if conn:
                        conn.close()

      def cerrar_sesion(self):
            try:
                  confirm = self.centrar_messagebox("yesno", "Cerrar sesión", "¿Estás seguro de que deseas cerrar sesión?")
                  if confirm:
                        self.usuario_id = None
                        self.reserva_id = None
                        self.silla_seleccionada = None
                        self.hora_actual = None

                        if hasattr(self, 'cantina_frame'):
                              self.cantina_frame.pack_forget()
                              self.reservar_frame.pack_forget()
                              self.mostrar_logo()
                              self.mostrar_login()
            except Exception as e:
                  self.centrar_messagebox("Error, ""Error inesperado", f"Se produjo un error al cerrar sesión: {str(e)}")            # Obtener las dimensiones de la ventana principal
      
      def centrar_messagebox(self, tipo, titulo, mensaje):
            
            self.update_idletasks() 
            ventana_x = self.winfo_x()
            ventana_y = self.winfo_y()
            ventana_ancho = self.winfo_width()
            ventana_alto = self.winfo_height()

            center_x = ventana_x + ventana_ancho // 2
            center_y = ventana_y + ventana_alto // 2

            dummy = customtkinter.CTkToplevel(self)
            dummy.geometry(f"1x1+{center_x}+{center_y}") 
            dummy.overrideredirect(True)  
            dummy.lift()  
            dummy.withdraw() 

            if tipo == "info":
                  messagebox.showinfo(titulo, mensaje, parent=dummy)
            elif tipo == "warning":
                  messagebox.showwarning(titulo, mensaje, parent=dummy)
            elif tipo == "error":
                  messagebox.showerror(titulo, mensaje, parent=dummy)
            elif tipo == "yesno":
                  return messagebox.askyesno(titulo, mensaje, parent=dummy)

      
            dummy.destroy()
if __name__ == "__main__":
    app = App()
    app.mainloop()