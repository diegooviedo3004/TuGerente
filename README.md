# TuGerente
Prueba técnica para TuGerente

# API Hotel
Endpoints principales (en orden de funcionamiento):

## Clientes

Es necesario que exista un cliente para crear una reservación.

```/api/client ```
Retorna una lista de los clientes existentes
Permite crear un cliente

```/api/client/<id>```
Retorna un cliente en especifico.
Actualiza un cliente / Elimina un cliente
  
## Métodos de pago
  
```/api/payment```
Retorna la lista de metodos de pago actuales [GET]  
Permite crear un método de pago [POST]
  
```/api/payment/<id>```
Retorna un metodo de pago en especifico. [GET]  
Actualiza un metodo de pago [PATCH,PUT] / Elimina un metodo de pago [DELETE]
  
> Decidí trabajar los metodos de pago y los status en tablas separadas, para que sea sencillo el crear nuevos datos.
 
## Status

```/api/status/```
Retorna la lista de posibles status de reservación [GET]  
Permite crear un status [POST]

```/api/status/<id>```
Retorna un status en especifico. [GET]  
Actualiza un status [PATCH,PUT] / Elimina un status [DELETE]
  
## Reservaciones
  
```/api/reservation/```
Retorna la lista de reservaciones [GET]  
Permite crear una nueva reservacion [POST]
  
```/api/reservation/<id>```
Retorna una reservación en especifico. [GET]  
Actualiza una reservación [PATCH,PUT] / Elimina una reservación [DELETE]
  


# Base de datos
SQLite (Django default)
Los campos created_at, updated_at, son autogenerados por Django, así que no será necesario enviarlos.


![Database Diagram](https://i.ibb.co/YNrkBGC/draw-SQL-export-2022-09-10-19-53.png)
