# mutant-detector

## Para correr los tests
1. Con su entorno local activado y en la carpeta mutant-detector/mutant ejecute ```pytest detector/tests.py ``` 

## Si desea levantar el servicio de manera local, siga las siguientes instrucciones:

1. Clone el repositorio desde la rama master.
2. Asegurese que tiene una interpete de Python 3.9 instalado, asi como la herramienta ```pipenv```.
3. Asegurese que tiene una instancia de postgres local y es accesible.
4. Asegurese de tener un entorno virtual creado, si no es asi, ejecute ```pipenv shell``` para crearlo.
5. Con el entorno de ejecucion activado, en la carpeta ```mutant-detector``` ejecute la instruccion ```pipenv install```
6. Modifique el contenido del archivo .env.local con su configuracion de acceso a la instancia de postgres presente en su maquina.
7. Con el entorno de ejecucion activado, en la ruta ```mutant-detector/mutant``` ejecute ```./manage.py migrate``` para ejecutar la migracion que creara las tablas necesarias.
8. Con el entorno de ejecucion activado, en la ruta ```mutant-detector/mutant``` ejecute ```./manage.py runserver 0.0.0.0:70000``` para levantar el servicio localmente.

## Si desea levantar el servicio de manera remota, siga las siguientes instrucciones:

1. Ingrese al servidor remoto via ssh. Asegurese de que tiene acceso a internet desde el servidor para poder descargar las dependencias necesarias por el proyecto.
2. Clone el repositorio desde la rama master. Debera tener docker y docker-compose instalados, asi como permisos de ejecucion con el usuario que ingresa al servidor.
3. En la ruta recien clonada ```mutant-detector```, ejecute ```docker-compose up &```. Esto creara el contenedor y levantara el servicio.

## Si desea probar el servicio desde AWS o localmente, siga las siguientes instrucciones:

1. Usando Postman, importe los archivos mercado_libre.postman_environment.json y MercadoLibreTest.postman_collection.json
2. Ejecute cualquiera de las peticiones que vienen configuradas en el collections que acaba de importar. Use las variables de entorno para probar localmente (```local```) o desde AWS (```dev```)
