import usuarios.usuario as modelo

class Acciones:

    def registro(self):

        print(f"Ok!! vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        # Le enviamos a la clase Usuario() los datos de los atributos.
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            #print(registro[0])
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!!")

 
    def login(self):

        print(f"Ok!! Identificate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}\n")

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Email ó Contraseña incorrectos...")
            