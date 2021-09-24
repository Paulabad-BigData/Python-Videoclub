class Pelicula():
    
    def __init__(self, codigo, titulo, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero

    def mostrar_pelicula(self):
        print("Codigo: ", self.codigo)
        print("Titulo: ", self.titulo)
        print("Genero: ", self.genero)
