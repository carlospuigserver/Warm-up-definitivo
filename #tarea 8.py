#tarea 8(Introducción a las funciones , proyecto bitcoin):
#En esta tarea haremos un programa que nos dirá cuando el valor del bitcoin cae a menos de 30.000 euros
#Necesitamos crear una función para pasar de bitcoin a Euros
#Si el bitcoin es inferior a 40.000 euros, hay que escribir un mensaje de alarma
#Un bitcoin está valorado en 25.000 euros

def BitcoinToEuros(bitcoin_amount,bitcoin_value_euros):
   valor=bitcoin_amount * bitcoin_value_euros
   return valor
   
    