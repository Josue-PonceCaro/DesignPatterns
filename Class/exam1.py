class User:
    varx = 10  # VARIABLE DE CLASE
    def __init__(self,username,password, email):
        self.username = username #ATRIBUTOS
        self.__password = self.__password_generator(password)
        self.email = email
    def __password_generator(self,password): # METODOS
        return password.upper()
    def get_password(self):
        return self.__password
pepe = User('pepito', 'pepito123', 'pepe@pepito.com') # INSTANCIA
print(pepe.username)
print(pepe.get_password())