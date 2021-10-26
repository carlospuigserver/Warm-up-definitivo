#tarea 5 (Operadores lógicos y booleanos):

precio=100 # =100

x=precio + (precio*20/100) # =120


y=x + (x*20/100) # =144


z=y + (y*20/100) # =172.8

pagar= precio + x + y + z 

if pagar >= 0 and pagar <= 2000:
    print("No nos quedamos sin dinero")

# El porcentaje de hambre(phi) es 17%, y cada vez que compremos un helado(4 veces), se sumará este 17 al anterior, hasta que esta cifra esté entre 85-100
# porcentaje hambre inicial,precio,x,y,z(phi), (php), (phx), (phy), (phz)
phz=17
phi=php=phx=phy=phz
phtotal = phi+php+phx+phy+phz
if phtotal >= 85 and phtotal <= 100 :
    print("No nos vamos a quedar con hambre")

#En la sintaxis he empleado diferentes variables para poder realizar operaciones lógicas, más el término if , utilizado para imprimir las respuestas basadas en unas condiciones, para condicionar estos datos he tenido que usar algunas operaciones lógicas