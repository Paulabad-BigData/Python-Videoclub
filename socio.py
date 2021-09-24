class Socio(): # clase se define el nombre con la primera en mayuscula
    def __init__(self, codigo, nombre, telefono, domicilio): # se define el constructor con el objeto
        self.codigo = codigo # atributos publicos
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

    def mostrar_socio(self):
        print("Codigo: ", self.codigo)
        print("Nombre: ", self.nombre)
        print("Telefono: ", self.telefono)
        print("Domicilio: ", self.domicilio)

        # self.__codigo = codigo estos son atributos privados se diferencia de los publicos por el guion abajo
        # get y set se utilizan para atributos privados