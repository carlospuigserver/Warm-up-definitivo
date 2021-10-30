#tareaa 5 

#  17=17%=porcentaje de hambre inicial
#  17*5=85
#  17*6=102
#De esta manera vemos que el porcentaje de hambre debe ser de un 85%

if 17*5 >=85 and 17*5<=100:
    print("Tenemos que comprarnos 4 helados y sumarnos el hambre inicial, y estaremos llenos (85-100%")
if 17*6>100:
    print("De hecho comernos 4 helados es la única forma de llenarnos")


#Ahora veremos como de llenos estamos comprando 4 helados
hambre=17
while hambre<85:
    hambre=hambre+17
    
    
print(hambre )
print("Como hemos llegado a un 85%, no nos quedaremos con hambre")


#De esta manera, cada vez que se suma un 17% para estar entre el 85% y el 100% de porcentaje de hambre 
# se está comprando un helado, por eso para quedarnos llenos empezando con un 17% de hambre,
# se deberán comprar 4 helados

#Ahora calcularemos el precio de la compra de 4 helados

precio=100
x=(precio*20/100)+precio
y=(x*20/100)+x
z=(y*20/100)+y
pagar=precio+x+y+z
print(pagar)
if pagar>=0 and pagar <=2000:
    print("Como hemos pagado menos de 2000 euros no nos quedamos sin dinero")
else:
    print("Te has quedado sin dinero")
        











