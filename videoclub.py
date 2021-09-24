from socio import Socio
from pelicula import Pelicula

class VideoClub():
    def __init__(self, nombre):
        self.nombre = nombre
        self.socios = []
        self.peliculas = []

    def buscar_socio(self, codigo):
        for i in range(len(self.socios)):
            if self.socios[i].codigo == codigo:
                return i # i es la posicion siempre y cuando el codigo que llega es igual
        return -1 # lo que me enviaron por codigo es igual a -1 se debe almacenar en la lista

    def adicionar_socio(self, socio):
        if self.buscar_socio(socio.codigo) == -1: # buscar_socio es un metodo
            self.socios.append(socio)
            return True
        return False


    def listar_socio(self):
        for socio in self.socios:
            print("*******************************")
            socio.mostrar_socio()
    

    def eliminar_socio(self, codigo):
        pos = self.buscar_socio(codigo)  #estamos buscando por posición
        if pos != -1:
            del(self.socios[pos])
            return True
        return False

    def buscar_pelicula(self, codigo):
        for i in range(len(self.peliculas)):
            if self.peliculas[i].codigo == codigo:
                return i # retorna la posición de la pelicula
        return -1
    
    def adicionar_pelicula(self, pelicula):
        if self.buscar_pelicula(pelicula.codigo) == -1:
            self.peliculas.append(pelicula) 
            return True
        return False

    def listar_pelicula(self):
        for pelicula in self.peliculas:
            print("*******************************")
            pelicula.mostrar_pelicula()

    def eliminar_pelicula(self, codigo):
        pos = self.buscar_pelicula(codigo)
        if pos != -1:
            del(self.peliculas[pos])
            return True
        return False