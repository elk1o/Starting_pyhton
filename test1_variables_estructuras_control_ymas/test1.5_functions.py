#elk1o
def myfunction():
    return 'Hello world'

print myfunction()

def yourName(nombre,apellido):
    return 'Your name is %s %s' % (nombre,apellido)

frase = yourName('Erik','flores')
print frase
#Functions with default parameters. If this parameters are set in the call, the function get the value of the call.
def msgName(nombre,mensaje='Hola, '):
    return mensaje+nombre

print msgName('Erik')
print msgName('Erik','Buenas, que tal,')
print msgName(mensaje='Surprise! ',nombre='Its me!')

#Functions with unset number of parameters. Gets it like a Tuple
def runArbitraryParameters(fijo,*variables):
    print fijo
    #Tuple of arbitrary parameters
    for i in variables:
        print i
runArbitraryParameters('Hello','Flor','Ainara','Rober','J')

#Passing parameters with an Tuple
def calcular(importe,descuento):
    return importe - ( importe*descuento / 100 )
datos = [1500,10]
print calcular(*datos)

#Passing parameters with a Dict
def calcular(importe,descuento):
    return importe - ( importe*descuento / 100 )
datos = {"descuento":10,"importe":1500}
print calcular(**datos)

#Callback calls. Call a function inside other.
def funcion():
    print "Hi!,"
def saludar(nombre,mensaje="Hola"):
    print mensaje,nombre
    print funcion()
saludar('Laura')

#Dinamic function calls. The function's name is unknowed. locals() (local enviroment) and globals() (global enviroment)
def funcionHello():
    return 'Hello!!'
def callback(func=''):
    """LLamada de retorno a nivel global"""
    return globals()[func]()
print callback('funcionHello')

#Dinamic function calls with parameters
def funcionHello(nombre):
    return 'Hello!! '+nombre
def callback(func=''):
    """LLamada de retorno a nivel global"""
    return globals()[func]('Erik')
print callback('funcionHello')

#Check if function exists and is callable
if 'funcionHello' in locals():
    if callable(locals()['funcionHello']):
        print locals()['funcionHello']("Francisco")
    else:
        print 'Not callable function'
else:
        print 'Function not found'

#Recursive functions

def jugar(intento=1):
    respuesta = raw_input("De que color es una naranja?")
    if respuesta != "naranja":
        if intento < 3:
            print "Fallaste, intentalo de nuevo"
            intento += 1
            jugar(intento)
        else:
            print "You lose!"
    else:
        print "You win"
jugar()