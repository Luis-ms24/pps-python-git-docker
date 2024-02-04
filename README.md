# La Bayeta de la Fortuna

## Descripción
La Bayeta de la Fortuna es una aplicación web sencilla que te dice un texto auspicioso aleatorio cada vez que la visitas. Es una aplicación al estilo de galleta de la fortuna o servilleta de bar, que te puede alegrar el día o hacerte reflexionar.

## Uso
Para usar la aplicación, solo tienes que acceder a la URL donde está desplegada y ver el mensaje que te aparece. Puedes recargar la página para ver otro mensaje diferente.

## Tecnologías
La aplicación está desarrollada usando Python, Git y Docker. Python es el lenguaje de programación que se usa para generar los mensajes aleatorios. Git es el sistema de control de versiones que se usa para gestionar el código fuente. Docker es la plataforma que se usa para crear, ejecutar y distribuir la aplicación usando contenedores.

## Dependencias
- Para resolver las dependencias de este proyecto, se recomienda usar un entorno virtual de Python con venv.
- Para crear y activar un entorno virtual de Python con venv, sigue estos pasos:
    - Abre tu terminal y sitúate en la carpeta del proyecto
    - Ejecuta el comando `python3 -m venv env`. Esto creará una carpeta llamada env dentro de tu proyecto, donde se guardará el entorno virtual
    - Ejecuta el comando `source env/bin/activate`. Esto hará que tu terminal use el Python y los paquetes que hay en tu entorno virtual, en lugar de los que hay en tu sistema.
    - Para desactivar el entorno virtual, ejecuta el comando `deactivate`. Esto hará que tu terminal vuelva a usar el Python y los paquetes que hay en tu sistema.
- Para instalar las dependencias de este proyecto, usa el comando `pip install -r requirements.txt`. Esto instalará los paquetes que se especifican en el fichero requirements.txt. Este fichero contiene los nombres y las versiones de los paquetes que se usan en este proyecto

## Ejecución
- Para ejecutar la aplicación, asegúrate de que tu entorno virtual está activo y ejecuta el comando `python3 app.py`. Esto iniciará la aplicación web en el puerto 5000 de tu ordenador
- Para acceder a la aplicación, abre tu navegador y escribe la dirección http://127.0.0.1:5000/. Verás el mensaje "Hola, mundo" en la página principal
- Para obtener frases auspiciosas, accede a la ruta http://127.0.0.1:5000/frotar/<n_frases>, donde <n_frases> es el número de frases que quieres obtener por ejemplo http://127.0.0.1:5000/frotar/3. Verás una respuesta en formato JSON con la lista de frases

## Funcionalidades
- Este proyecto te permite crear y usar una aplicación web con Flask, que te muestra mensajes y frases auspiciosas
- La aplicación web tiene dos rutas:
    - /: Te muestra el mensaje "Hola, mundo"
    - /frotar/<n_frases>: Te devuelve una lista de frases auspiciosas en formato JSON, elegidas al azar de un fichero de texto
- La aplicación web usa la función frotar del fichero bayeta.py, que se encarga de generar y devolver las frases auspiciosas

## Construcción de la imagen con Docker
- Para construir la imagen de la aplicación, asegúrate de tener instalado Docker en tu máquina y ejecuta el comando `docker build -t nombre .`, reemplazando nombre por el nombre que quieras darle a tu imagen. Por ejemplo, puedes usar `docker build -t bayeta-fortuna-app .`

### Despliegue del contenedor
- Para desplegar un contenedor con la imagen que has creado, ejecuta el comando `docker run -p puerto:5000 nombre`, reemplazando puerto por el puerto que quieras usar en tu máquina, y nombre por el nombre de la imagen que has creado. Por ejemplo, puedes usar `docker run -p 8000:5000 bayeta-fortuna-app`
- Esto creará y ejecutará un contenedor con la imagen que has creado, y lo asociará al puerto que has elegido en tu máquina.

### Acceso a la aplicación
- Para acceder a la aplicación, abre tu navegador y escribe la dirección http://localhost:puerto/, reemplazando puerto por el puerto que has usado en el paso anterior. Por ejemplo, si has usado el puerto 8000, puedes usar http://localhost:8000/
- Verás el mensaje "Hola, mundo" en la página principal.
- Para obtener frases auspiciosas, accede a la ruta http://localhost:8000/frotar/<n_frases>, donde <n_frases> es el número de frases que quieres obtener por ejemplo http://localhost:8000/frotar/3. Verás una respuesta en formato JSON con la lista de frases.

## Uso de MongoDB y Docker
- Para usar MongoDB y Docker, asegúrate de tener instalados ambos en tu máquina y ejecuta el comando `docker network create nombre`, reemplazando nombre por el nombre que quieras darle a la red. Por ejemplo, puedes usar `docker network create bayeta_net`
- Esto creará una red con el nombre que le has dado, que permitirá la comunicación entre los contenedores de la aplicación y de MongoDB.
- Esto creará y ejecutará un contenedor con la imagen oficial de MongoDB, y lo asociará al puerto y a la red que has elegido.
- Conectamos mongodb con el contenedor `docker network connect bayeta_net mongo`

### Construcción de la imagen
- Para construir la imagen de la aplicación, ejecuta el comando `docker build -t nombre .`, reemplazando nombre por el nombre que quieras darle a tu imagen. Por ejemplo, puedes usar `docker build -t mongo_bayeta .`

### Despliegue del contenedor
- Para desplegar un contenedor con la imagen que has creado, ejecuta el comando `docker run -p puerto:5000 --network nombre nombre`, reemplazando puerto por el puerto que quieras usar en tu máquina, nombre por el nombre de la red que has creado, y nombre por el nombre de la imagen que has creado. Por ejemplo, puedes usar `docker run -p 8000:5000 --network bayeta_net mongo_bayeta`
- Esto creará y ejecutará un contenedor con la imagen que has creado, y lo asociará al puerto y a la red que has elegido.

### Acceso a la aplicación
- Para acceder a la aplicación, abre tu navegador y escribe la dirección http://localhost:puerto/, reemplazando puerto por el puerto que has usado en el paso anterior. Por ejemplo, si has usado el puerto 8000, puedes usar http://localhost:8000/
- Verás el mensaje "Hola, mundo" en la página principal.
- Para obtener frases auspiciosas, accede a la ruta /frotar/<n_frases>, donde <n_frases> es el número de frases que quieres obtener. Verás una respuesta en formato JSON con la lista de frases, elegidas al azar de la base de datos de MongoDB.

## Autor
La aplicación ha sido creada por Luis Eduardo Mosquera Sanchez, un estudiante del curso de Especialiazacion de Ciberseguridad del IES Ingeniero de la Cierva.
