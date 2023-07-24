# Telecomunicaciones

**Conciliacion Carrier Internacional:** Es un proceso que te permite a partir de unas lógicas telco poder categorizar los eventos internacionales, ya sea roaming o no.
Esta categorización recoge la información en varios diccionarios de las variables que identifican la conexión del evento a una antena concreta, dichas categorizaciones se realizan buscando la coincidencia exacta entre las variables mencionadas y rangos de numeración. A partir de ahí, se le asigna un euro/min que permite asignarle el coste del proveedor al evento para poder conciliar la factura.

**Alarmas consumo:** En este proceso se crea la configuración al servidor SMTP, incorpora las credencias del email a traves de un fichero yaml y se aplican una seríe de lógicas para que configure el campo "FROM" y "SUBJECT" en función del operador. Además, hay un control mediante los except de los errores que puedan ocurrir durante el envio. En este punto se guarda en una lista todos los operadores que han sufrido un error en los envios de tal forma que cuando se termine de enviar todos los correos se pueda analizar y reenviar los operdores con error.

**Movimientos de portabilidad:** Este proceso permite recopilar de un directorio todos los ficheros que suministra el nodo central de portabilidad y generar una historico. Con la diferencia de que este proceso categoriza en funcion den nrn origen y destino el proveedor del que viene o va. Además, de alguna lógica más profunda con rangos de numeración en caso de que sean el primer movimiento de un msisdn.
