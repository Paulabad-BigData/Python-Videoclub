# vamos a crear la clase principal
# define apartado de trabajo
# se importa system
# self es un objeto

from os import system
from socio import Socio # archivo y clase
from videoclub import VideoClub
from pelicula import Pelicula

class Menu:
    def __init__(self, videoclub):
        self.videoclub = videoclub # estoy enviando un objeto videoclub

    def adicionar_socio(self):
        system("cls")
        print("*******************************")
        print("****    ADICIONAR SOCIO    ****")
        print("*******************************")
        # se recibe los datos
        codigo = input("Digite codigo del socio: ")
        nombre = input("Digite nombre del socio: ")
        telefono = input("Digite telefono del socio: ")
        domicilio = input("Digite domicilio del socio: ")        
        socio = Socio(codigo, nombre, telefono, domicilio) # socio en minuscula es una instancia

        # el objeto invoca un archivo videoclub y un metodo adicionar socio y la instancia (socio)
        if self.videoclub.adicionar_socio(socio):
            print("*******************************")
            print("Info - El socio fue adicionado correctamente")
            print("*******************************")
            input()

        else:
            print("*******************************")
            print("Infor el socio no se pudo adicionar")
            print("*******************************")
            input()
    
    def listar_socio(self):
        system("cls")
        print("*******************************")
        print("****    LISTAR SOCIO    ****")
        print("*******************************")
        self.videoclub.listar_socio()
        input()

    def eliminar_socio(self):
        system("cls")
        print("*******************************")
        print("****    ELIMINAR SOCIO    ****")
        print("*******************************")
        codigo = input("Digite el codigo del socio que desea eliminar: ")
        if self.videoclub.eliminar_socio(codigo):
            print("*******************************")
            print("Info - El socio fue eliminado correctamente")
            print("*******************************")
            input()

        else:
            print("*******************************")
            print("Info el socio no se pudo eliminarr")
            print("*******************************")
            input()
    

    def adicionar_pelicula(self):
        system("cls")
        print("*******************************")
        print("****   ADICIONAR PELICULA  ****")
        print("*******************************")
        codigo = input("Digite el codigo de la Pelicula: ")
        titulo = input("Digite el titulo de la pelicula: ")
        genero = input("Digite el genero de la pelicula: ")
        pelicula = Pelicula(codigo, titulo, genero)
        if self.videoclub.adicionar_pelicula(pelicula):
            print("***********************************************")
            print("Info - La pelicula fue adicionada correctamente")
            print("***********************************************")
            input()

        else:
            print("***************************************")
            print("Info - La pelicula no se pudo adicionar")
            print("***************************************")
            input()

    def listar_pelicula(self):
        system("cls")
        print("*******************************")
        print("****    LISTAR PELICULAS   ****")
        print("*******************************")
        self.videoclub.listar_pelicula() # en videoclub esta el metodo para listar peliculas
        input()

    def eliminar_pelicula(self):
        system("cls")
        print("*******************************")
        print("****   ELIMINAR PELICULA  *****")
        print("*******************************")
        codigo = input("Digite el codigo de la Pelicula que desea eliminar: ")
        if self.videoclub.eliminar_pelicula(codigo): # en videoclub esta el metodo para eliminar
            print("*******************************")
            print("Info - La Pelicula fue eliminado correctamente")
            print("*******************************")
            input()

        else:
            print("*******************************")
            print("Info - La Pelicula no se pudo eliminarr")
            print("*******************************")
            input()


    # se define el metodo
    def mostrar_menu_principal(self):
        while True:
            system("cls")   # miestra no se haga nada vuelve a la pantalla inicial
            print("*******************************")   # decoradorees
            print("*******************************")
            print("******    VIDEOCLUB      ******")
            print("*******************************")
            print("*******************************")
            print("        Menu Principal")
            print("*******************************")
            print("*******************************")
            print(" 1 = Crear Socio")
            print(" 2 = Listar Socios")
            print(" 3 = Eliminar Socio")
            print("----------------")
            print(" 4 = Crear Pelicula")
            print(" 5 = Listar Peliculas")
            print(" 6 = Eliminar Pelicula")
            print("----------------")
            print(" 7 = Salir")
            print("*******************************")
            print("*******************************")

            try:
                print("*******************************")
                op = int(input("Digite su opción: "))  # para recibir la variable que envia el usuario y se lleva a una condición
                print("*******************************")


                if op == 1:
                    self.adicionar_socio() # estoy llamando una función
                
                elif op == 2:
                    self.listar_socio()
                
                elif op == 3:
                    self.eliminar_socio()

                elif op == 4:
                    self.adicionar_pelicula()
                
                elif op == 5:
                    self.listar_pelicula()

                elif op == 6:
                    self.eliminar_pelicula()

                elif op == 7:
                    break

                else:
                    print("*******************************")
                    print("Error - Opcion de menu invalida")
                    print("*******************************")
                    input()

            except ValueError:
                print("*******************************")
                print("Error - El valor debe ser un numero entero")
                print("*******************************")
                input()

if __name__ == '__main__':
    videoclub = VideoClub("ABC")
    menu = Menu(videoclub) 
    menu.mostrar_menu_principal()