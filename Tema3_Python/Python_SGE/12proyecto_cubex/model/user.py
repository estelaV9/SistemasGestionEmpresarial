class user:
    def __init__(self, email, password,name_user = None):
        """ Nota: Python no permite sobrecargar metodos como en otros lenguajes
        pero se puede manejar la creacion de objetos con diferentes parametros
        usando valores por defecto """
        self.name_user = name_user # SI NO SE PASA EL NOMBRE DE USUARIO, SERA NONE POR DEFECTO
        self.password = password
        self.email = email

    # CONVERTIR UN OBJETO A DICCIONARIO
    def to_dict(self):
        return {
            "Name": self.name_user,
            "Email": self.email,
            "Password": self.password
        }

    def __str__(self):
        # DEVOLVER INFO SOBRE USUARIO
        return f"Name: {self.name_user}, Password: {self.password}, Email: {self.email}"
