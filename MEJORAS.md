# Mejoras
1. Aniadir un archivo requirements.txt
Este archivo debe contener todas las dependencias a instalar del proyecto.
2. Aniadir un archivo .gitignore
Ignorar la carpeta en la que se ubica el virtual environment. Esto ayuda a reducir el peso del repositorio.
3. Renombrar Query Mysql.txt a init_db.SQL
Asi, podras usar el auto completado de tu editor de codigo.
4. Separar las variables de configuracion del proyecto (secret_key, acceso a la base de datos) de tu aplicacion. Es muy importante que las cadenas de conexion a la BD, no esten en tu repositorio (y mas aun, si es publico). Esto tambien permite que tu proyecto tenga diferentes configuraciones (produccion, desarrollo, etc).
Estas variables deben ser importadas de preferencia a traves de variables de entorno.
5. Tener mucho cuidado al escribir consultas SQL directamente.
Las funciones delete_contact y get_contact, son vulnerables a ataques de injeccion sql. Recuerda siempre usar queries parametrizadas cuando escribas sql puro (tip: sobretodo cuando se recibe informacion desde el cliente).
Para escribir una tupla de 1 elemento, se puede escribir como `(elemento_1, )`
6. Se aniadio flake8 como dependencia, para verificar errores de PEP8

(Perdon por las tildes y enies.)