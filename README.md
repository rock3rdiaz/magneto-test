# mutant-detector

## Si desea levantar el servicio de manera local, siga las siguientes instrucciones:

1. Clone el repositorio desde la rama master
2. Modifique el contenido del archivo .env.local acorde a la configuracion de su maquina.
3. En la raiz del proyecto, ejecute la instruccion docker-compose -f docker-compose.yml -f docker-compose.local.yml up. Esta instruccion levantara el contenedor usando la configuracion definida en el archivo de configuracion local que acaba de modificar.
4. Usando cualquier herramienta, ejecute alguna de las instrucciones que aparecen en la guia de la prueba.

## Si desea probar el servicio desde AWS, siga las siguientes instrucciones:

1. Usando Postman, importe los archivos mercado_libre.postman_environment.json y MercadoLibreTest.postman_collection.json
2. Ejecute cualquiera de las peticiones que vienen configuradas en el collections que acaba de importar.
