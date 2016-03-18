print('Test 1: Erik')

nombre_variable = 'Test 2: Erik'
print(nombre_variable)

# En la segunda asignacion machaca valor y tipo de la variable
nombre_variable = 3
print(nombre_variable)

# Concatenacion de strings y integer
a = 3
b = 5
cad = 'Test 3:'
print("%s La suma de %d y %d es %d" % (cad, a, b, a + b))

# Conversion de string a unicode ( aceptar acentos .. etc )
tilde = u'canci\xf3n'
print(tilde)

# Asignacion de variables multiple
a, b, c = 'string', 15, True
print(a)
print(b)
print(c)

# Asignacion de variables multiples con tuplas/listas
mi_tupla = ('hello world', 2016)
text, year = mi_tupla
print(text)
print(year)

# Operaciones matematicas
monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print(monto_neto)
