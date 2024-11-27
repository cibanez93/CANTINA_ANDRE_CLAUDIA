import customtkinter
from PIL import Image

class App(customtkinter.CTk):
      
      def __init__(self):
        super().__init__()

        self.title("Cantina") 
        self.geometry("1200x720") 
        self.resizable(False,False)

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
        self.naranja_oscuro ="#BB794E"
        self.gris_oscuro="#404040"
        self.gris_ultra_oscuro="#242424"
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
                                                             text_color=self.blanco,command=self.mostrar_cantina)
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
                                                           text_color=self.verde)
        self.crear_cuenta_button.pack(pady=20)

        volver_image = customtkinter.CTkImage(Image.open("img/flecha.png"),
                                              size=(20,20))
        self.volver_button = customtkinter.CTkButton(self.register_frame,
                                                     fg_color=self.naranja,
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
        
        perfil_image = customtkinter.CTkImage(Image.open("img/perfil.png"),
                                               size=(50,50))    
        self.mostrar_perfil_button=customtkinter.CTkButton(self.cantina_frame,
                                                           text="👤",
                                                           font=(self.tamaño_h1,30),
                                                           corner_radius=25,
                                                           border_width=1,
                                                           fg_color=self.gris_oscuro,
                                                           border_color=self.blanco,
                                                           bg_color=self.gris_oscuro,
                                                           width=25,
                                                           height=25)
        self.mostrar_perfil_button.place(x=1090,y=10)


        #boton 1 silla redonda blanca 
        
        self.sitio1_button=customtkinter.CTkButton(self,text="1",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1, 
                                                   self.tamaño_h1),corner_radius=30,
                                                   fg_color=self.gris_oscuro,
                                                   border_color=self.blanco,
                                                   bg_color=self.gris_oscuro,
                                                   border_width=4,
                                                   width=70,
                                                   height=70,
                                                   command=self.reservar)
        self.sitio1_button.place(x=250,
                                 y=90)

        #boton 2  silla redonda blanca
        self.sitio2_button=customtkinter.CTkButton(self,
                                                   text="2",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1,self.tamaño_h1),
                                                   corner_radius=30,
                                                   fg_color=self.gris_oscuro,
                                                   border_color=self.blanco,
                                                   bg_color=self.gris_oscuro,
                                                   border_width=4,
                                                   width=70,
                                                   height=70,
                                                   command=self.reservar)
        self.sitio2_button.place(x=100,
                                 y=225)

        #boton 3  silla redonda blanca 
        self.sitio3_button=customtkinter.CTkButton(self,
                                                   text="3",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1, self.tamaño_h1),
                                                   corner_radius=30,
                                                   fg_color=self.gris_oscuro,
                                                   border_color=self.blanco,
                                                   bg_color=self.gris_oscuro,
                                                   border_width=4,
                                                   width=70,
                                                   height=70,
                                                   command=self.reservar)
        self.sitio3_button.place(x=1050,
                                 y=340)

        #boton 4 silla 1 marron
        self.sitio4_button=customtkinter.CTkButton(self,
                                                   text="4",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1,self.tamaño_h1),
                                                   corner_radius=10,
                                                   fg_color=self.gris_oscuro,
                                                   border_color=self.blanco,
                                                   bg_color=self.gris_oscuro,
                                                   border_width=4,
                                                   width=80,
                                                   height=80,
                                                   command=self.reservar)
        self.sitio4_button.place(x=800,
                                 y=85)
        

        #boton 5 silla 2 marron
        self.sitio5_button=customtkinter.CTkButton(self,
                                                   text="5",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1,self.tamaño_h1),
                                                   corner_radius=10,
                                                   fg_color=self.gris_oscuro,
                                                   border_color=self.blanco,
                                                   bg_color=self.gris_oscuro,
                                                   border_width=4,
                                                   width=80,
                                                   height=80,
                                                   command=self.reservar)
        self.sitio5_button.place(x=800,
                                 y=227)

        #boton 6 silla 3 marron
        self.sitio6_button=customtkinter.CTkButton(self,
                                                   text="6",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1, 
                                                   self.tamaño_h1),
                                                   corner_radius=10,
                                                   fg_color=self.gris_oscuro,
                                                   border_color=self.blanco,
                                                   bg_color=self.gris_oscuro,
                                                   border_width=4,
                                                   width=80,
                                                   height=80,
                                                   command=self.reservar)
        self.sitio6_button.place(x=429,
                                 y=85)

        #boton 7 silla 4 marron
        self.sitio7_button=customtkinter.CTkButton(self,text="7",
                                                   text_color=self.blanco,
                                                   font=(self.fuente_h1,
                                                   self.tamaño_h1),
                                                   corner_radius=10,
                                                   fg_color=self.gris_oscuro,
                                                   border_color=self.blanco,
                                                   bg_color=self.gris_oscuro,
                                                   border_width=4,
                                                   width=80,
                                                   height=80,
                                                   command=self.reservar)
        self.sitio7_button.place(x=429,
                                 y=227) 

      def reservar(self):
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
                                                            hover_color=self.naranja_oscuro)
        self.aceptar_reserva_button.pack(pady=20,
                                         padx=0)



if __name__ == "__main__":
    app = App()
    app.mainloop()
