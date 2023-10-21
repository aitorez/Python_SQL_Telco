# Telecomunicaciones

## Proyecto Telecomunicaciones

En este proyecto se pretende crear un tarificador respetando ciertas lógicas telco, esto consiste en construir unas cdrs que conformen nuestra tabla de mediación. Para ello se va a construir una servidor local desde SQLlite para una vez creada la tabla introducirla mediante terminal en un servidor. Tras construir esto se aplicará las lógicas de interconexión para conciliar las facturas que suelen aparecer con los OMR (Operadores Móviles de red).

Para ello la estructura del proyecto es:

- Para construir servidor SQLlite:

	. **conection_sql_lite.py:** Se crean las funciones que se llamaran en main_menu para poder interactuar con el servidor.
	. **main_menu.py:** Se crea el interfaz y se llama a las funciones para poder interactuar y hacer las siguientes funcionalidades:
				
			. Crear un servidor
			. Crear una tabla en el servidor indicado a través de un dataframe (pandas)
			. Borrar, actualizar o remplazar una determinada tabla
			. Consultar las tablas existentes en un determinado servidor
			. Salir del servidor

	. **cdr_national_simulator:** Se crean unas CDRS de tipología nacional incluyendo eventos de red inteligente.Respetando lógicas MOC/MTC

	. **cdr_international_simulator:** Se crean unas CDRS de tipología internacional. Respetando lógicas MOC/MTC
	
	. **functions.py:** Se crean funciones útiles para agilizar la manipulación de los datos.



## Utiles Telecomunicaciones


**Conciliación Carrier Internacional:** Es un proceso que te permite a partir de unas lógicas telco poder categorizar los eventos internacionales, ya sea roaming o no.
Esta categorización recoge la información en varios diccionarios de las variables que identifican la conexión del evento a una antena concreta, dichas categorizaciones se realizan buscando la coincidencia exacta entre las variables mencionadas y rangos de numeración. A partir de ahí, se le asigna un euro/min que permite asignarle el coste del proveedor al evento para poder conciliar la factura.

**Alarmas consumo:** En este proceso se crea la configuración al servidor SMTP, incorpora las credencias del email a través de un fichero yaml y se aplican una seríe de lógicas para que configure el campo "FROM" y "SUBJECT" en función del operador. Además, hay un control mediante los except de los errores que puedan ocurrir durante el envio. En este punto se guarda en una lista todos los operadores que han sufrido un error en los envios de tal forma que cuando se termine de enviar todos los correos se pueda analizar y reenviar los operadores con error.

**Movimientos de portabilidad:** Este proceso permite recopilar de un directorio todos los ficheros que suministra el nodo central de portabilidad y generar una histórico. Con la diferencia de que este proceso categoriza en función del nrn origen y destino el proveedor del que viene o va. Además, de alguna lógica más profunda con rangos de numeración en caso de que sean el primer movimiento de un msisdn.
