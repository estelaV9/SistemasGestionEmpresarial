class user:
    def __init__(self, name_user, password, email):
        self.name_user = name_user
        self.password = password
        self.email = email

    # CONVERTIR UN OBJETO A DICCIONARIO
    def to_dict(self):
        return {
            "Name": self.name_user,
            "Password": self.password,
            "Email": self.email
        }

    def __str__(self):
        # DEVOLVER INFO SOBRE USUARIO
        return f"Name: {self.name_user}, Password: {self.password}, Email: {self.email}"
