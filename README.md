#### Restful CRUD API
*por Ishmeet Bindra*

**¿Qué vamos a aprender?**
- NoSQL
- REST
- Deploy
- CRUD Model

**¿Nos hace falta algo?**
- [Python 3.6 +](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [MongoDB](https://www.mongodb.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [PyMongo](https://pypi.org/project/pymongo/)
- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)


**¿A quién va dirigido este taller?**

Personas "familiarizadas" con los métodos HTTP.

**¡Empecemos!**

```
docker pull mongo

docker create -it --name xcontainer_name -p 5000:27017 mongo

docker start xcontainer_name

```
*Primer paso fundamental listo: MongoDB en un container y accesible desde el puerto `5000`*

*Para detener el container en cualquier momento: `docker stop xcontainer_name`*

### Importante

> **Structured Logging**
>
>> Starting in `MongoDB 4.4`, **`mongod / mongosinstances` output all log messages in structured JSON format**. Log entries are written as a series of key-value pairs, where each key indicates a log message field type,such as “severity”, and each corresponding value records the associated logging information for that field type, such as “informational”. *Previously, log entries were output as plaintext*.

**Seguir leyendo**

<details>
<summary markdown="span">Ver</summary>

<pre>
  LINK: <a href="https://docs.mongodb.com/manual/reference/log-messages/">Log Messages</a>
</pre>
</details>

**NOTA**

Se utilizó cada episodio como referencia. El resultado final difiere del contenido original. Si bien la aproximación al tema es la misma, el código fue ligeramente modificado, personalizado, para un mejor entendimiento.