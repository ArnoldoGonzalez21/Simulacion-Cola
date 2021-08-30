from ListaDoble import ListaDoble
pizzas = ListaDoble()

def ingresar_orden():
    nuevo_pedido = str(input('\nIngresar el ingrediente que desea para la pizza: '))
    pizzas.insertar(nuevo_pedido)
    print('\n\tPedido recibido de una pizza de '+ nuevo_pedido)
    
def entregar_orden():
    orden_entrega = pizzas.extraer()
    if orden_entrega is None:
        print('\n\tCola vacía - Totalidad de órdenes entregadas')
    else:
        print('\n\tEntrega de una orden de pizza de '+ orden_entrega)

def mostrar_orden():
    ordenes = pizzas.mostrar_ordenes()
    if ordenes is False:
        print('\n\tCola vacía - Totalidad de órdenes entregadas')

def datos_estudiante():
    datos = '''\t> Arnoldo Luis Antonio González Camey
    \t> 201701548
    \t> Introducción a la Programación y Computación 2 Sección \"D\"
    \t> Ingeniería en Ciencias y Sistemas
    \t> 6to Semestre'''
    print(datos)

def pedir_numero():
    correcto = False
    numero = 0
    while(not correcto):
        try:
            correcto = True
            numero = int(input("Elige una opción: "))            
        except ValueError:
            print('Elige un número')
    return numero

def main():
    termino = False
    opcion = 0   
    while not termino:
        print('\n<<<<<<<<<< Menú >>>>>>>>>>')
        print ("1. Ingresar Orden")
        print ("2. Entregar Orden")
        print ("3. Mostrar Ordenes")
        print ("4. Mostrar Datos del Estudiante")
        print ("5. Salir")
        opcion = pedir_numero() 
        if opcion == 1:
            ingresar_orden()
        elif opcion == 2:
            print('\nEntregar Orden:')
            entregar_orden()
        elif opcion == 3:
            print('\nÓrdenes sin entregar:')
            mostrar_orden()
        elif opcion == 4:
            print('\nDatos del Estudiante:')
            datos_estudiante()
        elif opcion == 5:
            print('**Saliendo**')
            termino = True
            exit() 
        else:
            print('Elige una opción correcta')
            
if __name__ == '__main__':
    main()   