#tarea10 (importaciones en python)

def bitcoinToEuros(bitcoin_value_euros,bitcoin_amount):
    euros_value=bitcoin_value_euros*bitcoin_amount
    if euros_value<30000:
        print("El precio del bitcoin ha caido por debajo de los 30.000 Euros")
    else:
        print("Por ahora no hay que preocuparse , el precio del bitcoin se mantiene superior a 30.000") 
        

bitcoinToEuros(1,25000)

