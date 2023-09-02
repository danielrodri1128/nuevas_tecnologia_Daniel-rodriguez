# reciban el valor d euna compra 
# que puedan ingresar el numero de cuotas 
# calcular el valor de la cuota 
# usando while queremos q imprima el plan de pago y le muestre el cupo liberado con cada pago 

valorcompra = float(input("ingrese el valor de la compra"))
numcuotas = int ("ingrese el numero d ecuotas")
valorcuotas = valorcompra / numcuotas
cuota_actual = 1
saldo_restante = valorcompra

while cuota_actual <= numcuotas:
    print(f"cuota {cuota_actual}:  valor de cuota = {valorcuotas: .2f} saldo restante = {saldo_restante:.2f}")
    cuota_actual +=1
    saldo_restante -= valorcuotas
    