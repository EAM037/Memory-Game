import turtle
import random

def escojer_color(lista_colores):#la función crea una lista nueva que selecciona 9 colores de la lista de colores original
    listaNew= []
    random.shuffle(lista_colores)
    for i in range (9):
        listaNew.append(lista_colores[i])
    return listaNew

def posiciones(listaC):#la función crea una lista con los numeros de los colores
    listaNew=[]
    num= len(listaC)
    for i in range(num):
        listaNew.append(i)
    return listaNew

def cuadrados(lista):#la funcion crea 9 cuadrados de colores distintos
    turtle.speed(20)
    cuadros= 0
    for color in lista:
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(180)
        turtle.end_fill()
        turtle.pu()
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.pd()
        turtle.color("white")
        turtle.write(str(color),False,align="left",font=("Arial",20,"normal"))
        turtle.pu()
        turtle.left(180)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        if cuadros==2 or cuadros==5:
            turtle.left(180)
            turtle.forward(210)
            turtle.left(90)
            turtle.forward(105)
            turtle.left(90)
            turtle.pd()
            cuadros= cuadros +1
        else:
            turtle.forward(105)
            turtle.pd()
            cuadros= cuadros+1

def numeros(pos):#la función numera el orden de los colores
    cuadrados= 0
    turtle.pu()
    turtle.left(180)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(310)
    turtle.left(90)
    turtle.forward(310)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)
    for i in range(len(pos)):
        turtle.write(i,False,align="left",font=("Arial",20,"normal"))
        if cuadrados==2 or cuadrados==5:
            turtle.left(180)
            turtle.forward(215)
            turtle.left(90)
            turtle.forward(105)
            turtle.left(90)
            turtle.forward(5)
            cuadrados= cuadrados+1
        else:
            turtle.forward(105)
            cuadrados= cuadrados+1

def sombreado():#la función crea un cuadrado que cubre todos los demas cuadrados
    turtle.speed(5)
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(235)
    turtle.left(90)
    turtle.forward(310)
    turtle.right(180)
    turtle.pd()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(310)
    turtle.right(90)
    turtle.forward(310)
    turtle.right(90)
    turtle.forward(310)
    turtle.right(90)
    turtle.forward(310)
    turtle.right(90)
    turtle.end_fill()
    
def resultados(nombre, puntos):#la funcion crea una lista con el nombre de el jugador y su puntuaje obtenido
    lista_results= []
    lista_results.append(nombre)
    lista_results.append(puntos)
    return lista_results

def escribe(dif,results):#la funcion escribe los resultados en el archivo de resultados correspondiente
    if dif==1:
        with open("Resultados_facil.txt") as archivo:
            s= archivo.read()
            s= s + "\n" + str(results)
        f=open("Resultados_facil.txt","w")
        f.write(s)
        f.close()
    elif dif==2:
        with open("Resultados_intermedio.txt") as archivo:
            s= archivo.read()
            s= s + "\n" + str(results)
        f=open("Resultados_intermedio.txt","w")
        f.write(s)
        f.close()
    elif dif==3:
        with open("Resultados_dificil.txt") as archivo:
            s= archivo.read()
            s= s + "\n" + str(results)
        f=open("Resultados_dificil.txt","w")
        f.write(s)
        f.close()

def lee_arch(dif):#la funcion lee y muestra la hoja de resultados correspondiente
    if dif==1:
        with open("Resultados_facil.txt") as archivo:
            lineas= archivo.read()
        print(lineas)
    elif dif==2:
        with open("Resultados_intermedio.txt") as archivo:
            lineas= archivo.read()
        print(lineas)
    elif dif==3:
        with open("Resultados_dificil.txt") as archivo:
            lineas= archivo.read()
        print(lineas)
    
    
def main():
    nombre= input("¿Cuál es tu nombre? ")
    print("Seleccione una dificultad antes de comezar")
    print("1)Fácil")
    print("2)Intermedio")
    print("3)Díficil")
    dificultad= int(input())
    input("Oprime enter para empezar")
    lista_colores=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray"]
    #lista de todos los colores posibles
    lista_mixta= escojer_color(lista_colores) #se crea una nueva lista que contiene solo nueve valores revueltos de la lista anterior
    cuadrados(lista_mixta)#se dibujan los cuadrados
    pos= posiciones(lista_mixta)#se crean una lista con los numeros de los colores
    numeros(pos)#se enumeran los colores
    lista_colores=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray"]
    if dificultad == 1:
        print("Estos son los colores:", random.sample(lista_mixta, k=9))
        print("Nota: la lista mostrada no esta en orden")
    elif dificultad == 2:
        print("Estos son todos los posible colores:",lista_colores)
        print("Nota: la lista tambien contiene los colores que no fueron mostrados")
    elif dificultad == 3:
        print("Nota: La dificultad díficil no ofrece una lista de opciones")
        #se mostrara una lista de opciones segun la dificultad elegida antes de empezar
    input("Oprime enter cuando estes listo para jugar ")
    puntos= 0
    sombreado()#se cubren los cuadrados
    for i in range(9):
        print("¿Cual fue el color numero", i,"?")
        color= input()
        if color == lista_mixta[i]:
            puntos= puntos + 10
            print("Correcto, sumaste 10 puntos")
        else:
            print("Respuesta incorrecta")
    #se le pedira al jugador los nombres de los colores en el orden que fueron enumerados
    results=resultados(nombre,puntos)#se registraran los resultados en una lista
    print("Tus puntos finales: ", puntos)#se le mostraron los puntos conseguidos al jugador
    if puntos == 90:
        print("Felicitaciones, tienes una excelente memoria")
    else:
        print("Prueba a intentalo otra vez")
    escribe(dificultad,results)#se escriben los resultados en el archivo correspondiente
    print("Todos los resultados")
    lee_arch(dificultad)#se lee el archivo donde fueron escritos sus resultados
           
main()