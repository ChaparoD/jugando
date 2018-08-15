#wena qlo

class Matriz:
    def __init__(self):
        ejemplo=[[0,0,0],[0,0,0],[0,0,0]]
        self.matriz=ejemplo
        
    def __str__(self):
        k=""
        for i in range(3):
            for j in range(3):
                k+=str(self.matriz[i][j])+","
                if j==2:
                    k+="\n"
        return k
                    

    def rotar(self,lado):
        
        h=""
        for i in range(3):
            for j in range(3):
                m=self.matriz[i][j]
                h+=str(m)
        if str(lado)=="DERECHA": 
            
            l1=[]
            l2=[]
            l3=[]
            matriz_derecha=[]
            x=6
            for j in range(3):
                l1.append(int(h[x]))
                x=x-3
            x=7
            for j in range(3):
                l2.append(int(h[x]))
                x=x-3
            x=8
            for j in range(3):
                l3.append(int(h[x]))
                x=x-3
            matriz_derecha.append(l1)
            matriz_derecha.append(l2)
            matriz_derecha.append(l3)
            self.matriz=matriz_derecha
            return self.matriz
        elif str(lado)=="IZQUIERDA":
            l4=[]
            l5=[]
            l6=[]
            matriz_izquierda=[]
            x=2
            for j in range(3):
                l4.append(int(h[x]))
                x=x+3
            x=1
            for j in range(3):
                l5.append(int(h[x]))
                x=x+3
            x=0
            for j in range(3):
                l6.append(int(h[x]))
                x=x+3
            matriz_izquierda.append(l4)
            matriz_izquierda.append(l5)
            matriz_izquierda.append(l6)
            self.matriz=matriz_izquierda
            return self.matriz
        
            

            
   

class Tablero:
    def __init__(self,amplitud):
        self.t=[]
        self.amplitud=amplitud
        x=(self.amplitud/3)**2
        for i in range(int(x)):
            self.t.append(Matriz())
    def imprimir(self):
        h=""
        inicio=0
        final=int(self.amplitud/3)
        suma=int(self.amplitud/3)
        
        for primera_fila_de_matrices in range(int(self.amplitud/3)):
            for i in range(3):
                y=0
                for j in range(inicio,final):
                    h+="|"
                    m = self.t[j].matriz #acceder al objeto
                    for k in range(3):
                        h+=str(m[i][k])+","
                        y+=1
                        if k==2:
                            h=h[0:len(h)-1]
                        if y==self.amplitud:
                            h+="\n"
                            y=0
            inicio+=suma
            final+=suma
            multiplicador=int(6*(self.amplitud/3))
            h+="-"*multiplicador+"\n"
                    
        print(h)
    def guardar(self,nombre,n,m,turno,lista):
        tablero_guardado=open(str(nombre)+".txt","w")
        tablero_guardado.write(str(n)+","+str(m)+","+str(turno)+"\n")
        lista_jugadores=lista
        for elemento in lista_jugadores:
            tablero_guardado.write(elemento+"\n")
        
            
        
        h=""
        inicio=0
        final=int(self.amplitud/3)
        suma=int(self.amplitud/3)
        
        for primera_fila_de_matrices in range(int(self.amplitud/3)):
            for i in range(3):
                y=0
                for j in range(inicio,final):
                    
                    m = self.t[j].matriz #acceder al objeto
                    for k in range(3):
                        h+=str(m[i][k])+","
                        y+=1
                        if y==self.amplitud:
                            h=h[0:len(h)-1]
                            h+="\n"
                            tablero_guardado.write(h)
                            h=""
                            y=0
            inicio+=suma
            final+=suma
        tablero_guardado.close()
        
    def importar(self,archivo):
        
        importado=open(archivo+".txt","r")
        tablero_importado=importado.readlines()
        tablero_enlistas=[]
        for elemento in tablero_importado:
            minilista=elemento.strip().split(",")
            tablero_enlistas.append(minilista)
        tablero_vacio=Tablero(int(tablero_enlistas[0][0]))
        amplitud=int(tablero_enlistas[0][0])
        
        jugadores=int(tablero_enlistas[0][1])
        contador=1
        for i in range((jugadores+1),(jugadores+1+amplitud)):
            fila=tablero_enlistas[i]
            
            for k in range(amplitud):
                numero=int(fila[k])
                tablero_vacio.jugada(numero,contador,k+1)
            contador+=1
        importado.close()
        tablero_vacio.imprimir()
        
        return tablero_vacio
    def importar_amplitud(self,archivo):
        importado=open(archivo+".txt","r")
        tablero_importado=importado.readlines()
        tablero_enlistas=[]
        for elemento in tablero_importado:
            minilista=elemento.strip().split(",")
            tablero_enlistas.append(minilista)
        tablero_vacio=Tablero(int(tablero_enlistas[0][0]))
        amplitud=int(tablero_enlistas[0][0])
        return amplitud
                    







            
            
       
    def importar_jugadores(self,archivo):
        importado=open(archivo+".txt","r")
        tablero_importado=importado.readlines()
        tablero_enlistas=[]
        for elemento in tablero_importado:
            minilista=elemento.strip().split(",")
            tablero_enlistas.append(minilista)
        jugadores=int(tablero_enlistas[0][1])
        lista_jugadores=[]
        for elemento in range(1,jugadores+1):
            jugador=tablero_enlistas[elemento][0]
            lista_jugadores.append(jugador)
        importado.close()
        
        return lista_jugadores
    def importar_turno(self,archivo):
        importado=open(archivo+".txt","r")
        tablero_importado=importado.readlines()
        tablero_enlistas=[]
        for elemento in tablero_importado:
            minilista=elemento.strip().split(",")
            tablero_enlistas.append(minilista)
        turno=int(tablero_enlistas[0][2])
        return turno
        
    
        
    def jugada(self,numerojugador,x,y):
         
         f=x-1
         c=y-1
         n=self.amplitud/3
         h1=f//3
         k1=c//3
         posicion_matriz=int(n*h1+k1)
         h2=f%3
         k2=c%3
         if self.t[posicion_matriz].matriz[h2][k2]!=0:
             return False
         else:
             self.t[posicion_matriz].matriz[h2][k2]=numerojugador
         
         
         
    def girar(self,n,lado):
        LADO=str(lado.upper())
        self.t[n-1].rotar(LADO)
        
    def ceros_disponibles(self,tablero):
        abajo=1
        contador=0
        while abajo<=(self.amplitud):
                 
            check=1
            while check<=(self.amplitud):
                     
                if self.buscar(abajo,check)==0:
                    return True
                check+=1
            abajo+=1
        print(str(contador))
        return False
        
        
    def buscar(self,x,y):
         f=x-1
         c=y-1
         n=self.amplitud/3
         h=f//3
         k=c//3
         posicion_matriz=int(n*h+k)
         h2=f%3
         k2=c%3
         valor=self.t[posicion_matriz].matriz[h2][k2]
         
         return valor
        
    def juego_terminado(self,lista):
         
        self.jugadores=lista
         
        for elemento in self.jugadores:
             
            numero=self.jugadores.index(elemento)+1
            abajo=1
            while abajo<=(self.amplitud):
                 
                contador=0
                check=1
                while check<=(self.amplitud):
                     
                    if self.buscar(abajo,check)==numero:
                        contador+=1
                    if self.buscar(abajo,check)!=numero:
                        contador=0
                    if contador==5:
                        return True
                    check+=1
                abajo+=1
         #chequeo de columnas
        for elemento in self.jugadores:
             
            numero=self.jugadores.index(elemento)+1
            derecha=1
            while derecha<=(self.amplitud):
                 
                contador=0
                check=1
                while check<=(self.amplitud):
                     
                    if self.buscar(check,derecha)==numero:
                         contador+=1
                    if self.buscar(check,derecha)!=numero:
                        contador=0
                    if contador==5:
                        return True
                    check+=1
                derecha+=1
        #cheque diagonal negativa para abajo
        for elemento in self.jugadores:
             
            numero=self.jugadores.index(elemento)+1
            abajo=1
            while abajo<=(self.amplitud)-4:
                 
                contador=0
                derecha=1
                check=abajo
                while check<=(self.amplitud) and derecha<=(self.amplitud):
                     
                    if self.buscar(check,derecha)==numero:
                         contador+=1
                    if self.buscar(check,derecha)!=numero:
                        contador=0
                    if contador==5:
                        return True
                    check+=1
                    derecha+=1
                abajo+=1
        #chequeo diagonal negativa para la derecha
        for elemento in self.jugadores:
             
            numero=self.jugadores.index(elemento)+1
            derecha=1
            while derecha<=(self.amplitud)-4:
                 
                contador=0
                abajo=1
                check=derecha
                while check<=(self.amplitud) and abajo<=(self.amplitud):
                     
                    if self.buscar(abajo,check)==numero:
                        contador+=1
                    if self.buscar(abajo,check)!=numero:
                        contador=0
                    if contador==5:
                        return True
                    check+=1
                    abajo+=1
                derecha+=1
        #chequeo diagonal positiva para la izquierda
        for elemento in self.jugadores:
             
            numero=self.jugadores.index(elemento)+1
            derecha=self.amplitud
            while derecha>=5:
                 
                contador=0
                abajo=1
                check=derecha
                while check>=1 and abajo<=(self.amplitud):
                     
                    if self.buscar(abajo,check)==numero:
                         contador+=1
                    if self.buscar(abajo,check)!=numero:
                        contador=0
                    if contador==5:
                        return True
                    check-=1
                    abajo+=1
                derecha-=1        
            
        #cheque diagonal negativa hacia abajo
        for elemento in self.jugadores:
             
            numero=self.jugadores.index(elemento)+1
            abajo=1
            while abajo>=self.amplitud-4:
                 
                contador=0
                derecha=self.amplitud
                check=abajo
                while check<=self.amplitud and derecha>=1:
                     
                    if self.buscar(check,derecha)==numero:
                         contador+=1
                    if self.buscar(check,derecha)!=numero:
                        contador=0
                    if contador==5:
                        return True
                    check+=1
                    derecha-=1
                abajo+=1  

                 
              
                     
        
                    
                 
             
        

 
print("=========================================")       
print("\\\\\\\\\BIENBENIDOS A PENTAGON//////////")       
print("=========================================\n")   
print("INSTRUCCIONES:")
print("-------------\n")
print("- deberas ingresar las coordenas de donde desees jugar:")
print("columnas--> posicion horizontal")
print("filas-->posicion vertical\n")
print("- luego decidir que cuadrante desees rotar, el primero en formar")
print(" 5 numeros seguidos (horizontales, verticales o diagonales) GANA!\n")
print("Por ejemplo, si tu amplitud es de 9, el orden de los cuadrantes viene dado por:")
print(" 1 2 3")
print(" 4 5 6")
print(" 7 8 9\n")
print("para rotar en sentido horario--> derecha")
print("para rotar en sentido anti horario--> inzquierda\n")
print("QUE COMIENZE EL JUEGO!!")
print("=======================\n")
                           
import random
opcion=input("Desea Cargar una partida anterior, o Comenzar una nueva? (Cargar o nueva) :").lower()
if opcion=="nueva":
    
    while True:
        n=int(input("Amplitud del tablero? (multiplos de 3): "))
        if n%3!=0:
            print("Tu numero no es multiplo de 3, ingresa otro")
        else:
            break

    m=int(input("cuantos jugadores participaran? "))
    jugadores=[]


    for y in range(m):
        jugador=input("nombre del jugador ? ")
        jugadores.append(jugador.upper())
    jugadores_azar=[]
    while len(jugadores)>0:
        x=len(jugadores)
        azar=random.randint(0,(x-1))
        jugadores_azar.append(jugadores[azar])
        jugadores.pop(azar)

    tablero=Tablero(n)
    
    orden=""
    for elemento in jugadores_azar:
        orden+=elemento+" , "
    orden=orden[0:len(orden)-2]
    print("Orden de los Jugadores= "+orden+"\n")
        

    turno=1
    while tablero.ceros_disponibles(tablero)==True:
        guardadas=0
        nombre_partida=""
        for elemento in jugadores_azar:
            print("Jugador : "+str(elemento))
            print("Turno : "+str(turno))
            tablero.imprimir()
            respuesta=input("Desea guardar su partida? (si o no): ")
            if guardadas>0 and respuesta=="si":
                tablero.guardar(str(nombre_partida),n,m,turno,jugadores_azar)
                print("Guardado con exito")
            
            elif respuesta=="si":
                nombre_partida=input("Con que nombre quiere guardarla? ")
                tablero.guardar(str(nombre_partida),n,m,turno,jugadores_azar)
                print("Guardado con exito")
                guardadas+=1
            while True:
                columna=int(input("columna: "))
                fila=int(input("fila: "))
            
                jugador=jugadores_azar.index(elemento)+1
                if (tablero.jugada(jugador,fila,columna)==False) or (fila>n) or (columna>n) or (fila<0) or (columna<0):
                    print("coordenas ocupadas o incorrectas, elige otra ubicacion")
                else:
                    tablero.jugada(jugador,fila,columna)
                    break
            if tablero.juego_terminado(jugadores_azar)==True:
                print("Ha Ganado "+str(elemento)+"!!!!!")
                break
        
            tablero.imprimir()
            while True:
               bloque=int(input("bloque a girar(del 1 al "+str(int((n/3)**2))+") :"))
               lado=input("izquierda o derecha ?:")
               if bloque<0 or bloque>(int((n/3)**2)) or (lado!="izquierda" and lado!="derecha"):
                   print("numero fuera de rango, o lado mal escrito, vuelvelo a intentar!")
               else:
                   break
            tablero.girar(bloque,lado)
            if tablero.juego_terminado(jugadores_azar)==True:
                print("\n")
                print("Ha Ganado "+str(elemento)+"!!!!!")
                break
            if tablero.ceros_disponibles(tablero)==False:
                print("ya no quedan espacios disponibles")
                print("EMPATE!")
                break

            
        
           
        
        
            print("\n")
            print("-----------------------------------------------------")
            print("\n")
            turno+=1
        if tablero.juego_terminado(jugadores_azar)==True:
                print("\n")
                print("Estado final del Tablero:")
                tablero.imprimir()
                break

elif opcion=="cargar":
    archivo=input("Nombre de la partida guardada?")
    tablero=Tablero(12)
    tablero=tablero.importar(archivo)
    jugadores_azar=tablero.importar_jugadores(archivo)
    n=tablero.importar_amplitud(archivo)
    m=len(jugadores_azar)
    
    turno=tablero.importar_turno(archivo)
    
    orden=""
    for elemento in jugadores_azar:
        orden+=elemento+" , "
    orden=orden[0:len(orden)-2]
    print("Orden de los Jugadores= "+orden+"\n")
    while tablero.ceros_disponibles(tablero)==True:
       
        for elemento in jugadores_azar:
            print("Jugador : "+str(elemento))
            print("Turno : "+str(turno)+"\n")
            nombre_partida=archivo
            respuesta=input("Desea guardar su partida? (si o no): ")
           
            if respuesta=="si":
                tablero.guardar(str(nombre_partida),n,m,turno,jugadores_azar)
                print("Guardado con exito\n")
            tablero.imprimir()
            while True:
                columna=int(input("columna: "))
                fila=int(input("fila: "))
            
                jugador=jugadores_azar.index(elemento)+1
                if (tablero.jugada(jugador,fila,columna)==False) or (fila>n) or (columna>n) or (fila<0) or (columna<0):
                    print("coordenas ocupadas o incorrectas, elige otra ubicacion")
                else:
                    tablero.jugada(jugador,fila,columna)
                    break
            if tablero.juego_terminado(jugadores_azar)==True:
                print("Ha Ganado "+str(elemento)+"!!!!!")
                break
        
            tablero.imprimir()
            while True:
               bloque=int(input("bloque a girar(del 1 al "+str(int((n/3)**2))+") :"))
               lado=input("izquierda o derecha ?:")
               if bloque<0 or bloque>(int((n/3)**2)) or (lado!="izquierda" and lado!="derecha"):
                   print("numero fuera de rango, o lado mal escrito, vuelvelo a intentar!")
               else:
                   break
            tablero.girar(bloque,lado)
            if tablero.juego_terminado(jugadores_azar)==True:
                print("\n")
                print("Ha Ganado "+str(elemento)+"!!!!!")
                break
            if tablero.ceros_disponibles(tablero)==False:
                print("ya no quedan espacios disponibles")
                print("EMPATE!")
                break
                
        
        
            print("\n")
            print("-----------------------------------------------------")
            print("\n")
            turno+=1
        if tablero.juego_terminado(jugadores_azar)==True:
                print("\n")
                print("Estado final del Tablero:")
                tablero.imprimir()
                break
    
    
    
